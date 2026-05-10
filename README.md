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

![alt text](https://github.com/luisitoon28/rover_description/blob/main/entrega/graficas/analisis_final_completo.png "Logo de GitHub")

## 4. Explicación gráficas

### 4.1 cmd_vel

He añadido esta gráfica para que se vea lo comandado al rover.
Se puede observar en la velocidad lineal me he tenido que mover bastante hacia atrás, porque mi rover no rotaba muy bien si el terreno no era liso y tenia que moverme hacia abajo de la cuesta para rotar, se puede observar como cuando voy hacia atrás hay una velocidad angular para girar.

### 4.2 Posición de Rueda vs Tiempo

En esta gráfica podemos observar como y cuadno se desplaza el rover, cuando el valor en x es constante, es que el rover está parado, podemos ver 3 casos muy claros, uno al principio para coger el cubo verde y dejarlo en el envase, este el bastante largo porque hay que realizar muchos movimientos, uno en el medio, cogiendo el cubo azul y moviendo el brazo a la posición del cubo rojo y al final para dejar el cubo azul encima del rojo.
Entre estos momentos podemos ver como las posición de las ruedas varía ajustando la posición para realiar los movimientos con el scara y al final nos movemos hacia delante alrededor de 10m.

### 4.3 Acceleración vs Tiempo

Lo que podemos sacar de esta gráfica son los picos que acceleración, estos los vemos sobre todo cuando el robot cambia de velocidad brúscamente o no tanto. Los dos picos grandes que vemos, se pueden deber a que seguramente he realizado un cambio de velocidad brusco, por ejemplo, moviendome hacia atrás y sin que pare el rover, moviendolo hacia delante.
Cuando el esfuerzo o el cambio de velocidad es más grande, es cuando vemos los picos más altos, por ejemplo al final al subir la velocidad para recorrer los 10 metros, al realizar las rotaciones, o al pasar de parado a movimiento.

### 4.4 Gasto energético vs Tiempo

El gasto representa la potencia instantánea estimada en las ruedas. Cuando el rover está parado o se mueve poco, el gasto es bajo. En cambio, aparecen picos cuando el robot avanza, retrocede o intenta girar, porque los motores necesitan más esfuerzo. He intentado meter el meter el gasto del scara, pero este nunca se veia reflejado, el gasto es tan alto porque sumo el gasto de todas las ruedas.


## 5. Enlace rosbag

[rosbag](https://drive.google.com/drive/folders/1CXyFsugZ-jVsrXwYcGeEjOJEKXiLEylX?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto)
