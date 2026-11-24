Nombre del problema y asignatura.

"Simulador Automotriz"
Programación Aplicada II


Descripción y justificación.

Descripción del problema

El proyecto consiste en desarrollar un simulador de aceleración y movimiento de un automóvil utilizando el principio de Movimiento Rectilíneo Uniformemente Acelerado, este tipo de movimiento permite estudiar cómo cambia la velocidad de un automóvil cuando mantiene una aceleración constante durante un periodo determinado.

La aplicación permitirá ingresar datos como la velocidad inicial, la aceleración y el tiempo, a partir de estos valores el programa realizará diferentes cálculos para conocer la velocidad final, la distancia recorrida y el tiempo necesario para alcanzar una velocidad determinada.

Justificación

Este proyecto se relaciona con la carrera de Ingeniería Mecánica y Eléctrica, principalmente con el área de mecánica automotriz, ya que permite comprender y analizar el comportamiento de un automóvil durante su aceleración.

Además, permite aplicar los conocimientos adquiridos en Física sobre el movimiento, utilizando fórmulas matemáticas para resolver situaciones relacionadas con los vehículos, mediante Python, se busca automatizar estos cálculos y facilitar la comparación de diferentes situaciones de movimiento, utilizando la programación como una herramienta para resolver problemas de ingeniería.

Planteamiento original.

Un automóvil deportivo se encuentra circulando a una velocidad inicial de 20 km/h, al acelerar, alcanza una aceleración constante de 3 m/s² durante un periodo de 8 segundos, considerando que el automóvil realiza un Movimiento Rectilíneo Uniformemente Acelerado, se desea conocer cómo cambia su movimiento durante este tiempo.

Para resolver el problema se deben calcular los siguientes datos:

La velocidad final que alcanza el automóvil después de 8 segundos.

La distancia total que recorre durante ese periodo.

El tiempo que necesita para alcanzar una velocidad de 100 km/h.

La distancia que recorre desde el inicio hasta alcanzar los 100 km/h.

Para realizar los cálculos se utilizarán las ecuaciones de Movimiento Rectilíneo Uniformemente Acelerado, considerando que la aceleración permanece constante y que el automóvil se desplaza en línea recta.

Entradas del programa.

Nombre del automovil, Velocidad Inicial, Aceleración, Tiempo y Velocidad objetivo

Procesos y fórmulas.

1- Conversión de unidades

Primero, si el usuario ingresa la velocidad en kilómetros por hora, se convertirá a metros por segundo.

Fórmula: V = km/h ÷ 3.6

2- Cálculo de velocidad final

Se calculará la velocidad que alcanza el automóvil después de un determinado tiempo.

Fórmula: Vf = Vi + (a × t)

3- Cálculo de distancia recorrida

Se calculará la distancia que recorre el automóvil durante el tiempo de aceleración.

Fórmula: d = (Vi × t) + (1/2 × a × t²)

4- Cálculo del tiempo para alcanzar una velocidad determinada, se calculará cuánto tiempo necesita el automóvil para llegar a una velocidad objetivo.

Fórmula: t = (Vf - Vi) / a

5- Cálculo de distancia para alcanzar una velocidad determinada, se calculará la distancia necesaria para que el automóvil alcance una velocidad objetivo.

Fórmula: d = (Vf² - Vi²) / (2 × a)

Reglas y decisiones del programa

El programa deberá comprobar que los datos ingresados sean numéricos.

La velocidad inicial no podrá ser negativa.

La aceleración deberá ser mayor que cero.

El tiempo deberá ser mayor que cero.

La velocidad objetivo deberá ser mayor que la velocidad inicial.

Si el usuario ingresa una velocidad en km/h, se realizará la conversión correspondiente.

Si los datos no cumplen con las condiciones establecidas, el programa mostrará un mensaje de error y solicitará nuevamente la información.

Los resultados se mostrarán con dos decimales.

Proceso general

El usuario ingresará los datos del automóvil, seleccionará el cálculo que desea realizar y el programa aplicará la fórmula correspondiente, Finalmente, mostrará los resultados y permitirá realizar otra simulación o consultar los resultados anteriores.

Salidas esperadas.

Velocidad final: mostrará la velocidad que alcanza el automóvil después del tiempo establecido, expresada en m/s y km/h.

Distancia recorrida: indicará cuántos metros recorrió el automóvil durante el tiempo de aceleración.

Tiempo para alcanzar una velocidad determinada: mostrará cuántos segundos necesita el automóvil para llegar a la velocidad objetivo.

Distancia para alcanzar una velocidad determinada: indicará cuántos metros necesita recorrer el automóvil para llegar a la velocidad objetivo.

Historial de simulaciones: permitirá consultar los resultados de los cálculos realizados anteriormente.

Mensajes de validación: cuando el usuario ingrese datos incorrectos, el programa mostrará mensajes indicando el error y solicitará nuevamente la información.

Ejemplo original resuelto.

Nombre: Automóvil deportivo.

Velocidad inicial: 5.56 m/s.

Aceleración: 3 m/s².

Tiempo: 8 segundos.

Velocidad objetivo: 27.78 m/s.

El programa deberá mostrar:

Velocidad final: 29.56 m/s (106.42 km/h).

Distancia recorrida: 140.48 metros.

Tiempo para alcanzar 100 km/h: 7.41 segundos.

Distancia para alcanzar 100 km/h: 123.47 metros.

Alcance de la aplicación.

El programa permitirá realizar simulaciones del movimiento de un automóvil para conocer cómo aumenta su velocidad cuando mantiene una aceleración constante, el usuario podrá ingresar los datos necesarios y obtener diferentes resultados mediante cálculos automáticos.

Entre las funciones principales se encontrará el cálculo de la velocidad final, la distancia recorrida, el tiempo que tarda en alcanzar cierta velocidad y la distancia necesaria para llegar a ella, también contará con opciones para guardar las simulaciones realizadas y revisar los resultados anteriores.

Además, el sistema tendrá un menú para facilitar su uso y validará los datos ingresados para evitar errores durante los cálculos.

El programa se enfocará únicamente en movimientos en línea recta y con aceleración constante, por lo tanto, no tomará en cuenta otros factores que intervienen en el funcionamiento real de un automóvil, como el peso, la resistencia del aire, la fricción o las condiciones del camino.

Comprobación de requisitos técnicos.

El proyecto se desarrollará utilizando el lenguaje de programación Python y contará con una estructura organizada en diferentes archivos para facilitar su funcionamiento y comprensión.

Para cumplir con los requisitos técnicos establecidos, la aplicación incluirá los siguientes elementos:

Variables: se utilizarán para almacenar los datos del automóvil, como velocidad inicial, aceleración, tiempo y velocidad objetivo.

Operaciones matemáticas: se aplicarán las fórmulas del MRUA para obtener los resultados de cada simulación.

Condiciones: se utilizarán para comprobar que los datos ingresados sean correctos y cumplan con las restricciones del programa.

Ciclos: permitirán mantener el menú activo y repetir las operaciones hasta que el usuario decida salir.

Validaciones: evitarán que se ingresen datos vacíos, letras en campos numéricos o valores que no sean permitidos.

Listas: se utilizarán para almacenar los resultados de las simulaciones y consultar el historial.

Clases y objetos: el programa contará con al menos dos clases, cada una con una responsabilidad diferente.

Constructores y atributos: las clases utilizarán el método __init_ para inicializar sus datos y self para manejar sus atributos.

Métodos: cada clase tendrá funciones encargadas de realizar sus propias tareas.

Archivo principal: se utilizará un archivo main.py para mostrar el menú, recibir las opciones del usuario y coordinar el funcionamiento de las clases.

Módulos separados: las clases se guardarán en archivos independientes dentro de la carpeta clases/.