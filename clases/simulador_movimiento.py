
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
