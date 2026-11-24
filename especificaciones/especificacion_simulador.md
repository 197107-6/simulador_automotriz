1- Nombre de la clase

SimuladorMovimiento

2- Descripción

La clase SimuladorMovimiento será la encargada de realizar los cálculos relacionados con el Movimiento Rectilíneo Uniformemente Acelerado (MRUA). Utilizará los datos proporcionados por la clase Automovil para calcular la velocidad final, la distancia recorrida y los valores necesarios para alcanzar una velocidad determinada.

También permitirá almacenar los resultados de cada simulación para que el usuario pueda consultar las operaciones realizadas anteriormente.

3- Atributos

Atributo

Automovil
historial

Tipo de dato

automovil
list


4- Constructor

Se utilizará el método __init_ para recibir el objeto Automovil y crear una lista vacía donde se almacenarán los resultados de las simulaciones.

Se utilizará self para acceder a los atributos de la clase.

5- Métodos

calcular_velocidad_final(tiempo): calcula la velocidad final del automóvil utilizando la fórmula Vf = Vi + (a × t).

calcular_distancia(tiempo): obtiene la distancia recorrida mediante la fórmula d = (Vi × t) + (1/2 × a × t²).

calcular_tiempo_objetivo(velocidad_objetivo): calcula el tiempo necesario para alcanzar una velocidad determinada.

calcular_distancia_objetivo(velocidad_objetivo): calcula la distancia necesaria para alcanzar la velocidad objetivo.

guardar_resultado(resultado): almacena los resultados obtenidos en la lista del historial.

mostrar_historial(): muestra las simulaciones realizadas anteriormente.

6- Validaciones

El tiempo ingresado debe ser mayor que cero.

La velocidad objetivo debe ser mayor que la velocidad inicial.

La aceleración debe ser mayor que cero.

Los datos utilizados en las operaciones deben ser numéricos.

No se permitirán operaciones que provoquen una división entre cero.

7- Ejemplo de uso

Utilizando los datos de un automóvil deportivo:

Velocidad inicial: 5.56 m/s.

Aceleración: 3 m/s².

Tiempo: 8 segundos.

Velocidad objetivo: 27.78 m/s.

La clase realizará los cálculos y obtendrá los siguientes resultados aproximados:

Velocidad final: 29.56 m/s.

Distancia recorrida: 140.48 metros.

Tiempo para alcanzar la velocidad objetivo: 7.41 segundos.

Distancia para alcanzar la velocidad objetivo: 123.47 metros.