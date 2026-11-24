Necesito que desarrolles el código Python de la clase Automovil para mi Proyecto Integrador de Programación II.

Debes seguir exactamente las características que se encuentran en mi archivo especificacion_automovil.md y el análisis del problema de mi proyecto.

El proyecto consiste en un simulador de aceleración y movimiento de un automóvil utilizando las fórmulas del Movimiento Rectilíneo Uniformemente Acelerado (MRUA).

La clase debe cumplir con lo siguiente:

Crear una clase llamada Automovil.

Utilizar el constructor init.

Manejar los atributos nombre, velocidad_inicial y aceleracion utilizando self.

Crear el método convertir_kmh_a_ms() para convertir kilómetros por hora a metros por segundo, dividiendo entre 3.6.

Crear el método mostrar_datos() para mostrar la información del automóvil.

Validar que el nombre no esté vacío.

Validar que la velocidad inicial sea mayor o igual a cero.

Validar que la aceleración sea mayor que cero.

Utilizar nombres de variables y métodos en español.

Mantener el código sencillo, ordenado y adecuado para un estudiante de segundo semestre de Ingeniería Mecánica y Eléctrica.

No agregues funciones que no estén solicitadas. Entrega el código completo y explica brevemente cómo funciona.
Aquí tienes el código de la clase `Automovil` según las especificaciones que proporcionaste:

```python
class Automovil:
    def __init__(self, nombre, velocidad_inicial, aceleracion):
        # Validación del nombre
        if not nombre:
            raise ValueError("El nombre del automóvil no puede estar vacío.")
        self.nombre = nombre
        
        # Validación de la velocidad inicial
        if velocidad_inicial < 0:
            raise ValueError("La velocidad inicial debe ser mayor o igual a cero.")
        self.velocidad_inicial = velocidad_inicial
        
        # Validación de la aceleración
        if aceleracion <= 0:
            raise ValueError("La aceleración debe ser mayor que cero.")
        self.aceleracion = aceleracion

    def convertir_kmh_a_ms(self):
        """Convierte la velocidad de km/h a m/s."""
        return self.velocidad_inicial / 3.6

    def mostrar_datos(self):
        """Muestra la información del automóvil."""
        print(f"Nombre del automóvil: {self.nombre}")
        print(f"Velocidad inicial (km/h): {self.velocidad_inicial}")
        print(f"Aceleración (m/s²): {self.aceleracion}")
        print(f"Velocidad inicial (m/s): {self.convertir_kmh_a_ms()}")
