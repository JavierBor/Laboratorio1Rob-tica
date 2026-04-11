# Laboratorio1Rob-tica
# Laboratorio 1 - Robótica

## Integrantes
* **Diego Álvarez** (Analista)
* **Javier Bórquez** (Integrador)
* **Ariel Carrasco Suárez** (Documentador)
* **Benjamin Peredo** (Experimentador)
* **Diego Valenzuela** (Programador)

---

## Descripción del laboratorio
Este laboratorio consiste en la simulación de un robot móvil diferencial utilizando **Webots**. Un robot móvil diferencial utiliza dos ruedas motrices independientes a cada lado, y su movimiento depende de la velocidad de cada una.

### Especificaciones Técnicas
* **Robot utilizado:** e-puck.
* **Motores:** `left_motor` (izquierdo) y `right_motor` (derecho).
* **Lenguaje:** Python.
* **Controlador:** Permite definir velocidades iniciales, alterar el movimiento y evitar detenciones no deseadas.

---

## Instrucciones de Ejecución

1. **Obtener el código:** Abrir el link de GitHub y clonar el repositorio o descargar las carpetas.
2. **Cargar en Webots:** Abrir el proyecto y seleccionar la opción **E-puck "e-puck"** en el panel izquierdo.
3. **Configurar el controlador:** Asegurarse de que el robot tenga asignado el controlador `controladorLab1`.
4. **Modificar parámetros:** El código Python se visualiza a la derecha. Las **líneas 22 y 23** se utilizan para ajustar las velocidades de los motores y probar distintos comportamientos.

---

## Resultados Obtenidos

### Consideraciones Generales
* La velocidad base de prueba fue de **2.0** para avanzar en línea recta.
* El límite de velocidad del simulador es de **6.28**. Superar este valor genera una advertencia en la consola de Webots.

### Pruebas de Movimiento

| Prueba | Configuración | Comportamiento |
| :--- | :--- | :--- |
| **1** | `left_motor = right_motor` | El robot avanza en línea recta hasta chocar con la pared. |
| **2** | `left_motor != right_motor` | El robot realiza trayectorias circulares. |
| **3** | `right_motor = -left_motor` | El robot gira sobre su propio eje en el mismo lugar. |

#### Detalles de Giro:
* **Hacia la izquierda:** Ocurre cuando `left_motor < right_motor`.
* **Hacia la derecha:** Ocurre cuando `left_motor > right_motor`.
* **Sobre su eje:** Se logra aplicando valores negativos a uno de los motores (ej. `-2.0`).

> **Nota:** Se recomienda no utilizar valores de velocidad demasiado elevados para asegurar que la trayectoria sea fluida en la simulación.

---

## Preguntas de Análisis

1. **¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?**
   * El robot experimenta un movimiento lineal uniforme, es decir, avanza en línea recta.

2. **¿Cómo cambia la trayectoria cuando las velocidades son diferentes?**
   * El robot siempre pivotará (girará) hacia el lado de la rueda que se mueve más lento.

3. **¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?**
   * El robot gira sobre su propio eje central.

4. **¿Qué tipo de movimiento permite dibujar un círculo?**
   * Se requiere mantener velocidades constantes en ambas ruedas, pero con valores asimétricos entre ellas.
