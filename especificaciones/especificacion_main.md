1- Nombre del archivo

main.py

2- Descripción

El archivo principal será el encargado de controlar el funcionamiento general de la aplicación. Mostrará un menú en la consola para que el usuario pueda seleccionar las diferentes opciones disponibles.

También se encargará de solicitar los datos necesarios, crear los objetos de las clases Automovil y SimuladorMovimiento, y utilizar sus métodos para realizar las simulaciones.

3- Menú principal

El programa contará con las siguientes opciones:

Registrar los datos del automóvil.

Calcular la velocidad final.

Calcular la distancia recorrida.

Calcular el tiempo para alcanzar una velocidad determinada.

Calcular la distancia para alcanzar una velocidad determinada.

Consultar el historial de simulaciones.

Salir del programa.

4- Funcionamiento del programa

Al iniciar, se mostrará el menú principal.

El usuario seleccionará la operación que desea realizar.

El programa solicitará los datos necesarios para cada cálculo.

Se utilizarán los métodos de la clase SimuladorMovimiento para obtener los resultados.

Los resultados se mostrarán en la consola con dos decimales.

Cada simulación realizada se guardará en el historial.

El usuario podrá consultar los resultados anteriores.

El menú se repetirá hasta que se seleccione la opción de salir.

5- Clases utilizadas

Clase Automovil:

Se utilizará para registrar y almacenar el nombre del automóvil, su velocidad inicial y su aceleración.

Clase SimuladorMovimiento:

Se encargará de realizar las operaciones matemáticas del MRUA y almacenar los resultados de las simulaciones.

6- Validaciones

El menú solo aceptará opciones disponibles.

Los datos numéricos deberán ser válidos.

No se permitirán valores negativos cuando no correspondan.

Si el usuario ingresa una opción incorrecta, se mostrará un mensaje de error.

El programa solicitará nuevamente los datos cuando exista algún error.

7. Resultado esperado

Al ejecutar el archivo main.py, el usuario podrá acceder a un menú interactivo desde la consola, registrar un automóvil, realizar los cálculos de movimiento, consultar el historial y salir del programa cuando lo desee.