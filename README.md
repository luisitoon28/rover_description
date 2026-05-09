# Práctica 3 Modelado

Práctica realizada por Jose Luis Laria

## 0. Capturas Rviz

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/captura_rviz/captura_rviz.png
 "Captura rviz")

## 1. Capturas Simulación

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/capturas_simulacion/Captura_gazebo.png "Gazebo")

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/capturas_simulacion/cubo_verde.png  "Cogiendo el cubo verde")

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/capturas_simulacion/cubo_verde_2.png  "Cogiendo el cubo verde")

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/capturas_simulacion/dejando_cubo_verde.png  "Dejando el cubo verde")

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/capturas_simulacion/dejando_cubo_azul.png  "Dejando el cubo verde")


## 2. Árbol de transformadas

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/arbol_tf/frames.png "Árbol de tfs")

## 3. Gráficas

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/graficas/Figure_1.png "Logo de GitHub")

## 4. Explicación gráficas

### 4.1 Posición de Rueda vs Tiempo

En esta gráfica podemos observar cambios constantes de velocidad positivos y negativos, esto se deben a que para poder coger los cubos he tenido que dar marcha alante y atrás para ajustar la posición del rover. Y cuando está quieto es porque estoy moviendo el scara.

### 4.2 Acceleración vs Tiempo

Lo que podemos sacar de esta gráfica son los picos que acceleración, estos los vemos sobre todo cuando el robot cambia de velocidad brúscamente, es decir, al inico y final de las subidas y bajdas de velocidad de la gráfica anteriror. Los dos picos grandes que vemos, se pueden deber a que seguramente he realizado un cambio de velocidad brusco, por ejemplo, moviendome hacia atrás y sin que pare el rover, moviendolo hacia delante.

### 4.3 Gasto energético vs Tiempo

Como podemos observar el gasto se mantiene siempre a cero, esto se tiene que deber a algún fallo en la configuración del esfuerzo en el yaml del rover.


## 5. Enlace rosbag

[rosbag](https://drive.google.com/drive/folders/1kwHtYVWY_hUZ6L6eUPIMp7N4rGzGuf8L?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto)
