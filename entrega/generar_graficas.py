import matplotlib.pyplot as plt
from mcap_ros2_decoder import decode_ros2_messages
from datetime import datetime

# CONFIGURACIÓN
FILEPATH = "datos_robot_0.mcap"

# Diccionarios para almacenar datos
data = {
    'wheel_time': [], 'wheel_pos': [], 'wheel_power': [],
    'imu_time': [], 'imu_accel': []
}

print(f"Leyendo archivo: {FILEPATH}...")

# Leer los mensajes del MCAP
for decoded in decode_ros2_messages(FILEPATH):
    topic = decoded.topic
    msg = decoded.ros_msg
    # El timestamp del MCAP suele estar en nanosegundos
    t = decoded.publish_time.timestamp() 

    # 1. POSICIÓN DE RUEDAS Y GASTO (de /joint_states)
    if topic == "/joint_states":
        # Buscamos una de tus ruedas, por ejemplo la trasera izquierda
        if 'back_left_wheel_joint' in msg.name:
            idx = msg.name.index('back_left_wheel_joint')
            data['wheel_time'].append(t)
            data['wheel_pos'].append(msg.position[idx])
            # GASTO = Esfuerzo (Nm) * Velocidad (rad/s)
            potencia = abs(msg.effort[idx] * msg.velocity[idx])
            data['wheel_power'].append(potencia)

    # 2. ACELERACIÓN (de /imu)
    if topic == "/imu":
        data['imu_time'].append(t)
        data['imu_accel'].append(msg.linear_acceleration.x)

# Normalizar el tiempo (que empiece en 0)
if data['wheel_time']:
    t0 = min(data['wheel_time'][0], data['imu_time'][0] if data['imu_time'] else data['wheel_time'][0])
    data['wheel_time'] = [x - t0 for x in data['wheel_time']]
    data['imu_time'] = [x - t0 for x in data['imu_time']]

# --- GENERAR GRÁFICAS ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

# Gráfica 1: Posición de Ruedas
ax1.plot(data['wheel_time'], data['wheel_pos'], color='blue', linewidth=1.5)
ax1.set_title('Posición de Rueda vs Tiempo', fontsize=14)
ax1.set_ylabel('Posición (rad)')
ax1.grid(True, linestyle='--')

# Gráfica 2: Aceleración
ax2.plot(data['imu_time'], data['imu_accel'], color='red', linewidth=1)
ax2.set_title('Aceleración Lineal (Eje X) vs Tiempo', fontsize=14)
ax2.set_ylabel('Aceleración (m/s²)')
ax2.grid(True, linestyle='--')

# Gráfica 3: Gasto (Potencia instantánea)
ax3.plot(data['wheel_time'], data['wheel_power'], color='green', linewidth=1.5)
ax3.set_title('Gasto Energético (Potencia) vs Tiempo', fontsize=14)
ax3.set_ylabel('Potencia (W)')
ax3.set_xlabel('Tiempo (s)')
ax3.grid(True, linestyle='--')

plt.tight_layout()
plt.savefig('graficas_finales.png')
print("¡Hecho! Gráficas guardadas en 'graficas_finales.png'")
plt.show()
