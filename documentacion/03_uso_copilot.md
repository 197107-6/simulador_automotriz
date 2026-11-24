Uso de GitHub Copilot en el desarrollo del proyecto

1. Introducción

Durante el desarrollo del simulador de aceleración y movimiento de un automóvil se utilizó GitHub Copilot como herramienta de apoyo para la programación en Python.

Su función fue ayudar a generar código, organizar las clases, proponer métodos y corregir errores encontrados durante el desarrollo del programa.

2. Uso de Copilot

GitHub Copilot se utilizó en diferentes etapas del proyecto:

Creación de clases: ayudó a desarrollar la clase Automovil y la clase SimuladorMovimiento.

Desarrollo de métodos: apoyó en la creación de los métodos necesarios para calcular la velocidad final, distancia recorrida y tiempo para alcanzar una velocidad objetivo.

Validaciones: ayudó a implementar condiciones para evitar datos incorrectos.

Programa principal: se utilizó como apoyo para desarrollar el menú de opciones y conectar las dos clases.

3. Ejemplos

#Necesito que desarrolles el código Python de la clase Automovil para mi Proyecto Integrador de Programación II.

#Debes seguir exactamente las características que se encuentran en mi archivo especificacion_automovil.md y el análisis del problema de mi proyecto.

#El proyecto consiste en un simulador de aceleración y movimiento de un automóvil utilizando las fórmulas del Movimiento Rectilíneo Uniformemente Acelerado (MRUA).

#La clase debe cumplir con lo siguiente:

#Crear una clase llamada Automovil.

#Utilizar el constructor init.

#Manejar los atributos nombre, velocidad_inicial y aceleracion utilizando self.

#Crear el método convertir_kmh_a_ms() para convertir kilómetros por hora a metros por segundo, dividiendo entre 3.6.

#Crear el método mostrar_datos() para mostrar la información del automóvil.

#Validar que el nombre no esté vacío.

#Validar que la velocidad inicial sea mayor o igual a cero.

#Validar que la aceleración sea mayor que cero.

#Utilizar nombres de variables y métodos en español.

#Mantener el código sencillo, ordenado y adecuado para un estudiante de segundo semestre de Ingeniería Mecánica y Eléctrica.

#No agregues funciones que no estén solicitadas. Entrega el código completo y explica brevemente cómo funciona.
#Aquí tienes el código de la clase `Automovil` según las especificaciones que proporcionaste:

#```python

erjemplo #Desarrolla el archivo principal main.py para mi Proyecto Integrador de Programación II.

#Debes seguir exactamente mi archivo especificacion_main.md y utilizar las clases Automovil y SimuladorMovimiento que ya desarrollamos.

#El programa debe funcionar desde la consola de Python y contar con un menú interactivo.

#El menú debe tener estas opciones:

#Registrar los datos del automóvil.

#Calcular la velocidad final.

#Calcular la distancia recorrida.

#Calcular el tiempo para alcanzar una velocidad determinada.

#Calcular la distancia para alcanzar una velocidad determinada.

#Consultar el historial de simulaciones.

#Salir del programa.

#Requisitos:

#Importar las clases desde la carpeta clases.

#Solicitar el nombre, velocidad inicial y aceleración del automóvil.

#Permitir ingresar velocidades en km/h y convertirlas a m/s.

#Solicitar los datos necesarios para cada cálculo.

#Utilizar los métodos de SimuladorMovimiento para realizar las operaciones.

#Guardar los resultados de las simulaciones en el historial.

#Mostrar los resultados con dos decimales.

#Validar que los datos sean numéricos y que cumplan las restricciones del proyecto.

#Utilizar ciclos para mantener activo el menú.

#Utilizar condiciones para ejecutar cada opción.

#Mostrar mensajes de error cuando se ingresen datos incorrectos.

#No permitir realizar cálculos antes de registrar un automóvil.

#Mantener el código sencillo y organizado.

#No inventes otras funciones ni cambies las fórmulas documentadas. Entrega el código completo y explica cómo funciona.
#Aquí tienes el código completo para el archivo `main.py` según las especificaciones que proporcionaste:

#```python

5. Reflexión sobre el uso de Copilot

El uso de GitHub Copilot facilitó el desarrollo del proyecto porque permitió obtener ejemplos de código y resolver algunos problemas de programación, sin embargo, fue necesario revisar las respuestas de la herramienta, ya que no todo el código generado funcionaba correctamente desde el principio, esta experiencia permitió comprender que la inteligencia artificial puede ser una herramienta de apoyo para programar, pero es importante entender el código, revisar los resultados y comprobar que las operaciones sean correctas antes de utilizarlo.