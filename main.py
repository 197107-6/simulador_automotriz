
from clases.automovil import Automovil
from clases.simulador_movimiento import SimuladorMovimiento


def main():
    simulador = None

    while True:
        print("\nMenú:")
        print("1. Registrar automóvil")
        print("2. Calcular velocidad final")
        print("3. Calcular distancia recorrida")
        print("4. Calcular tiempo para alcanzar velocidad objetivo")
        print("5. Calcular distancia para alcanzar velocidad objetivo")
        print("6. Mostrar historial de simulaciones")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del automóvil: ")

            while True:
                try:
                    velocidad_inicial_kmh = float(
                        input("Ingrese la velocidad inicial (km/h): ")
                    )
                    if velocidad_inicial_kmh < 0:
                        raise ValueError(
                            "La velocidad inicial debe ser mayor o igual a cero."
                        )
                    velocidad_inicial_ms = velocidad_inicial_kmh / 3.6
                    break
                except ValueError as e:
                    print(f"Error: {e}. Intente nuevamente.")

            while True:
                try:
                    aceleracion = float(
                        input("Ingrese la aceleración (m/s²): ")
                    )
                    if aceleracion <= 0:
                        raise ValueError(
                            "La aceleración debe ser mayor que cero."
                        )
                    break
                except ValueError as e:
                    print(f"Error: {e}. Intente nuevamente.")

            try:
                automovil = Automovil(
                    nombre, velocidad_inicial_ms, aceleracion
                )
                simulador = SimuladorMovimiento(automovil)
                print("Automóvil registrado exitosamente.")
                automovil.mostrar_datos()
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            if not simulador:
                print("Debe registrar un automóvil primero.")
                continue

            tiempo = float(input("Ingrese el tiempo (s): "))

            try:
                velocidad_final = simulador.calcular_velocidad_final(tiempo)
                print(f"Velocidad final: {velocidad_final} m/s")
                simulador.guardar_resultado(
                    f"Velocidad final: {velocidad_final} m/s"
                )
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            if not simulador:
                print("Debe registrar un automóvil primero.")
                continue

            tiempo = float(input("Ingrese el tiempo (s): "))

            try:
                distancia = simulador.calcular_distancia(tiempo)
                print(f"Distancia recorrida: {distancia} m")
                simulador.guardar_resultado(
                    f"Distancia recorrida: {distancia} m"
                )
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            if not simulador:
                print("Debe registrar un automóvil primero.")
                continue

            velocidad_objetivo_kmh = float(
                input("Ingrese la velocidad objetivo (km/h): ")
            )
            velocidad_objetivo_ms = velocidad_objetivo_kmh / 3.6

            try:
                tiempo = simulador.calcular_tiempo_objetivo(
                    velocidad_objetivo_ms
                )
                print(
                    f"Tiempo para alcanzar la velocidad objetivo: {tiempo} s"
                )
                simulador.guardar_resultado(
                    f"Tiempo para alcanzar la velocidad objetivo: {tiempo} s"
                )
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "5":
            if not simulador:
                print("Debe registrar un automóvil primero.")
                continue

            velocidad_objetivo_kmh = float(
                input("Ingrese la velocidad objetivo (km/h): ")
            )
            velocidad_objetivo_ms = velocidad_objetivo_kmh / 3.6

            try:
                distancia = simulador.calcular_distancia_objetivo(
                    velocidad_objetivo_ms
                )
                print(
                    f"Distancia para alcanzar la velocidad objetivo: {distancia} m"
                )
                simulador.guardar_resultado(
                    f"Distancia para alcanzar la velocidad objetivo: {distancia} m"
                )
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "6":
            if not simulador:
                print("Debe registrar un automóvil primero.")
                continue

            simulador.mostrar_historial()

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
