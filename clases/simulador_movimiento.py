Ahora desarrolla la clase SimuladorMovimiento para mi Proyecto Integrador de Programación II.

Debes respetar mi archivo especificacion_simulador.md y utilizar la clase Automovil que ya desarrollamos en automovil.py.

La clase debe cumplir con lo siguiente:

Crear una clase llamada SimuladorMovimiento.

Utilizar el constructor init.

Recibir un objeto de la clase Automovil.

Crear una lista llamada historial para guardar los resultados de las simulaciones.

Utilizar self para manejar los atributos.

Crear el método calcular_velocidad_final(tiempo), utilizando la fórmula Vf = Vi + (a * t).

Crear el método calcular_distancia(tiempo), utilizando la fórmula d = (Vi * t) + (0.5 * a * t ** 2).

Crear el método calcular_tiempo_objetivo(velocidad_objetivo), utilizando la fórmula t = (Vf - Vi) / a.

Crear el método calcular_distancia_objetivo(velocidad_objetivo), utilizando la fórmula d = (Vf ** 2 - Vi ** 2) / (2 * a).

Crear el método guardar_resultado(resultado) para almacenar los resultados en la lista.

Crear el método mostrar_historial() para mostrar las simulaciones anteriores.

Validar que el tiempo sea mayor que cero y que la velocidad objetivo sea mayor que la velocidad inicial.

Mostrar los resultados con dos decimales.

Utiliza nombres en español y código sencillo para un estudiante de segundo semestre. No agregues funciones innecesarias. Entrega el código completo y explica cómo se relaciona con la clase Automovil.
Aquí tienes el código de la clase `SimuladorMovimiento` según las especificaciones que proporcionaste:
```python
class SimuladorMovimiento:
    def __init__(self, automovil):
        """Constructor que recibe un objeto de la clase Automovil."""
        self.automovil = automovil
        self.historial = []

    def calcular_velocidad_final(self, tiempo):
        """Calcula la velocidad final utilizando la fórmula Vf = Vi + (a * t)."""
        if tiempo <= 0:
            raise ValueError("El tiempo debe ser mayor que cero.")
        velocidad_final = self.automovil.velocidad_inicial + (self.automovil.aceleracion * tiempo)
        return round(velocidad_final, 2)

    def calcular_distancia(self, tiempo):
        """Calcula la distancia utilizando la fórmula d = (Vi * t) + (0.5 * a * t ** 2)."""
        if tiempo <= 0:
            raise ValueError("El tiempo debe ser mayor que cero.")
        distancia = (self.automovil.velocidad_inicial * tiempo) + (0.5 * self.automovil.aceleracion * tiempo ** 2)
        return round(distancia, 2)

    def calcular_tiempo_objetivo(self, velocidad_objetivo):
        """Calcula el tiempo necesario para alcanzar una velocidad objetivo."""
        if velocidad_objetivo <= self.automovil.velocidad_inicial:
            raise ValueError("La velocidad objetivo debe ser mayor que la velocidad inicial.")
        tiempo = (velocidad_objetivo - self.automovil.velocidad_inicial) / self.automovil.aceleracion
        return round(tiempo, 2)

    def calcular_distancia_objetivo(self, velocidad_objetivo):
        """Calcula la distancia necesaria para alcanzar una velocidad objetivo."""
        if velocidad_objetivo <= self.automovil.velocidad_inicial:
            raise ValueError("La velocidad objetivo debe ser mayor que la velocidad inicial.")
        distancia = (velocidad_objetivo ** 2 - self.automovil.velocidad_inicial ** 2) / (2 * self.automovil.aceleracion)
        return round(distancia, 2)

    def guardar_resultado(self, resultado):
        """Guarda un resultado en el historial."""
        self.historial.append(resultado)

    def mostrar_historial(self):
        """Muestra los resultados almacenados en el historial."""
        for i, resultado in enumerate(self.historial, start=1):
            print(f"Resultado {i}: {resultado}")
```