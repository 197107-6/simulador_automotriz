

class Automovil:
    def __init__(self, nombre, velocidad_inicial, aceleracion):
        
        if not nombre.strip():
            raise ValueError("El nombre del automóvil no puede estar vacío.")
        self.nombre = nombre
       
        
        if velocidad_inicial < 0:
            raise ValueError("La velocidad inicial debe ser mayor o igual a cero.")
        self.velocidad_inicial = velocidad_inicial
       
        
        if aceleracion <= 0:
            raise ValueError("La aceleración debe ser mayor que cero.")
        self.aceleracion = aceleracion

    def convertir_kmh_a_ms(self, velocidad_kmh):
        """Convierte una velocidad de km/h a m/s."""
        return velocidad_kmh / 3.6

    def mostrar_datos(self):
        """Muestra la información del automóvil."""
        print(f"Nombre del automóvil: {self.nombre}")
        print(f"Velocidad inicial (m/s): {self.velocidad_inicial:.2f}")
        print(f"Aceleración (m/s²): {self.aceleracion:.2f}")
