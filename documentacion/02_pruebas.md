Pruebas del simulador de aceleración y movimiento de un automóvil

1. Objetivo de las pruebas

El objetivo de las pruebas es comprobar que el programa funcione correctamente, que realice los cálculos de Movimiento Rectilíneo Uniformemente Acelerado (MRUA) y que valide los datos ingresados por el usuario.

También se busca verificar que las opciones del menú funcionen y que los resultados se almacenen correctamente en el historial de simulaciones.

2. Casos de prueba

Prueba 1. Registro del automóvil

**Datos de entrada:**
- Nombre: Automóvil deportivo.
- Velocidad inicial: 20 km/h.
- Aceleración: 3 m/s².

**Resultado esperado:**

El programa debe registrar el automóvil correctamente y convertir la velocidad inicial a 5.56 m/s.

**Resultado obtenido:**

El automóvil se registra correctamente y muestra sus datos.

**Estado:** Aprobada.

Prueba 2. Cálculo de velocidad final

**Datos de entrada:**
- Velocidad inicial: 5.56 m/s.
- Aceleración: 3 m/s².
- Tiempo: 8 segundos.

**Resultado esperado:**

29.56 m/s.

**Resultado obtenido:**

29.56 m/s.

**Estado:** Aprobada.

Prueba 3. Cálculo de distancia recorrida

**Datos de entrada:**
- Velocidad inicial: 5.56 m/s.
- Aceleración: 3 m/s².
- Tiempo: 8 segundos.

**Resultado esperado:**

140.48 metros.

**Resultado obtenido:**

140.48 metros.

**Estado:** Aprobada.

Prueba 4. Tiempo para alcanzar una velocidad objetivo

**Datos de entrada:**
- Velocidad inicial: 5.56 m/s.
- Aceleración: 3 m/s².
- Velocidad objetivo: 100 km/h (27.78 m/s).

**Resultado esperado:**

7.41 segundos.

**Resultado obtenido:**

7.41 segundos.

**Estado:** Aprobada.

Prueba 5. Distancia para alcanzar una velocidad objetivo

**Datos de entrada:**
- Velocidad inicial: 5.56 m/s.
- Aceleración: 3 m/s².
- Velocidad objetivo: 100 km/h (27.78 m/s).

**Resultado esperado:**

123.47 metros.

**Resultado obtenido:**

123.47 metros.

**Estado:** Aprobada.

Prueba 6. Aprobada

**Datos de entrada:**
- Velocidad inicial: -20 km/h.
- Aceleración: 0 m/s².

**Resultado esperado:**

El programa debe mostrar un mensaje de error y solicitar nuevamente los datos.

**Resultado obtenido:**

Se comprueba que las validaciones de las clases rechacen los valores no permitidos.

**Estado:** Aprobada

Prueba 7. Consulta del historial

**Datos de entrada:**

Se realizan los cuatro cálculos del ejercicio original y posteriormente se selecciona la opción 6.

**Resultado esperado:**

El programa debe mostrar los resultados almacenados en el historial.

**Resultado obtenido:**

El historial muestra las operaciones guardadas.

**Estado:** Pendiente de comprobar en ejecución.

3. Conclusión

Las pruebas permiten comprobar el funcionamiento del simulador y verificar que las fórmulas del MRUA se apliquen correctamente, también permiten identificar posibles errores en los datos ingresados y comprobar que las clases trabajen de manera conjunta.

Con estas pruebas se busca asegurar que el programa cumpla con las funciones establecidas en el análisis del problema y que pueda utilizarse para realizar simulaciones básicas del movimiento de un automóvil.