import csv
import matplotlib.pyplot as plt

tiempos = []
posiciones = []
gastos = []
aceleraciones = []

print("Procesando datos.csv...")

try:
    with open('datos.csv', mode='r') as f:
        # Usamos reader normal porque el CSV de ROS tiene cabeceras complejas
        reader = csv.reader(f)
        next(reader) # Saltamos la cabecera
        
        ultima_vel = 0
        
        for row in reader:
            if not row or len(row) < 20: continue
            
            try:
                # Según tu volcado:
                # La posición de las ruedas empieza aproximadamente en el índice 14-20
                # Vamos a tomar un valor representativo
                pos_rueda = float(row[16]) # back_left_wheel_joint (aprox)
                vel_rueda = float(row[28]) # velocidad (aprox)
                eff_rueda = float(row[40]) # esfuerzo (aprox)
                
                tiempos.append(len(tiempos))
                posiciones.append(pos_rueda)
                
                # Gasto energético (Potencia = Esfuerzo * Velocidad)
                # Si vel o eff son 'nan', usamos 0
                v = 0 if row[28] == 'nan' else vel_rueda
                e = 0 if row[40] == 'nan' else eff_rueda
                gastos.append(abs(e * v))
                
                # Aceleración (Derivada de la velocidad)
                aceleraciones.append(v - ultima_vel)
                ultima_vel = v
                
            except (ValueError, IndexError):
                continue

    if not tiempos:
        print("No se encontraron datos válidos. Revisa si el CSV tiene números.")
    else:
        plt.figure(figsize=(10, 12))

        # 1. Posición
        plt.subplot(3, 1, 1)
        plt.plot(tiempos, posiciones, color='blue')
        plt.title('Posición de Rueda vs Tiempo (Radianes)')
        plt.grid(True)

        # 2. Aceleración
        plt.subplot(3, 1, 2)
        plt.plot(tiempos, aceleraciones, color='red')
        plt.title('Aceleración vs Tiempo (m/s² aprox)')
        plt.grid(True)

        # 3. Gasto
        plt.subplot(3, 1, 3)
        plt.plot(tiempos, gastos, color='green')
        plt.title('Gasto Energético vs Tiempo (Watts)')
        plt.xlabel('Muestras')
        plt.grid(True)

        plt.tight_layout()
        plt.savefig('graficas_finales.png')
        print("¡CONSEGUIDO! Revisa el archivo 'graficas_finales.png'")
        plt.show()

except Exception as e:
    print(f"Error: {e}")
