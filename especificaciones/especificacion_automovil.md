1- Nombre de la clase

Automovil

2- Descripción

La clase Automovil se encargará de almacenar la información principal del vehículo que se utilizará en la simulación. Permitirá registrar su nombre, velocidad inicial y aceleración, además de realizar algunas conversiones de velocidad.

3- Atributos

Atributo

nombre
velocidad_inicial
aceleracion

Tipo de dato

str
float
float

4- Constructor

Se utilizará el método __init_ para recibir los datos iniciales del automóvil y guardarlos en sus respectivos atributos mediante self.

5- Métodos

convertir_kmh_a_ms(): convierte una velocidad de kilómetros por hora a metros por segundo.

mostrar_datos(): muestra el nombre, la velocidad inicial y la aceleración del automóvil.

6- Validaciones

El nombre del automóvil no debe estar vacío.

La velocidad inicial debe ser mayor o igual a cero.

La aceleración debe ser mayor que cero.

Los valores numéricos deben ser válidos.

7- Ejemplo de uso

Se registra un automóvil deportivo con los siguientes datos:

Nombre: Automóvil deportivo.

Velocidad inicial: 20 km/h.

Aceleración: 3 m/s².

El programa convertirá la velocidad inicial a metros por segundo, obteniendo aproximadamente 5.56 m/s, y almacenará los datos para utilizarlos en los cálculos de movimiento.