# Informe TP 2: Complejidad y Análisis de Rendimiento - BookMatch

## 1. Definición de la Operación Crítica
* **Operación elegida:** Búsqueda de libros por título (`buscar_por_titulo`).
* **Justificación técnica:** Se selecciona esta operación por ser la consulta más frecuente e importante para el usuario del sistema. Con un volumen pequeño de datos (como 20 elementos), una búsqueda secuencial es imperceptible; sin embargo, al escalar el sistema a 100.000 elementos, el tiempo de respuesta lineal se degrada de forma significativa ($O(n)$). Esto hace necesario e indispensable evaluar y comparar una estructura jerárquica basada en árboles para optimizar los tiempos de acceso.

## 2. Descripción de las Estrategias de Búsqueda

Para resolver la operación crítica de búsqueda por título, se implementaron dos enfoques contrastantes basados en la bibliografía de la materia:

- **Búsqueda Secuencial (Lineal):** Recorre la estructura de datos elemento por elemento de forma iterativa hasta encontrar la coincidencia exacta o agotar la lista. Su complejidad temporal en el peor caso es de $O(n)$.
- **Árbol Binario de Búsqueda (BST):** Organiza los elementos jerárquicamente manteniendo la invariante de que los subárboles izquierdos contienen claves menores y los derechos claves mayores. Esto permite aplicar división binaria del espacio de búsqueda, logrando una complejidad promedio de $O(\log n)$.

## 3. Metodología de Experimentación

Para evaluar el rendimiento empírico de ambos algoritmos, se diseñó el siguiente protocolo:
1. **Datasets de Prueba:** Se generaron tres volúmenes de datos sintéticos independientes mediante un script automatizado (`generador.py`), conteniendo $1.000$, $10.000$ y $100.000$ registros en formato JSON.
2. **Métricas Evaluadas:** 
   - **Pasos Lógicos:** Conteo de operaciones elementales (comparaciones y nodos visitados) para obtener una métrica matemática independiente del hardware.
   - **Tiempo de Ejecución:** Medición en milisegundos utilizando la función de alta precisión de Python (`time.time()`).
3. **Escenario de Evaluación:** Se evaluó el peor caso de búsqueda (buscando un elemento ubicado al final del conjunto o inexistente) para medir el impacto máximo del crecimiento de los datos ($n$).

## 4. Resultados Experimentales y Análisis de Rendimiento

Se realizaron pruebas empíricas evaluando el peor caso de búsqueda (buscando un elemento ubicado al final del dataset o inexistente) en tres volúmenes diferentes de datos:

| Tamaño del Dataset ($n$) | Búsqueda Secuencial (Pasos) | Búsqueda Secuencial (Tiempo) | Búsqueda BST (Pasos) | Búsqueda BST (Tiempo) |
| :--- | :--- | :--- | :--- | :--- |
| **1,000** | 999 | 0.0739 ms | 29 | 0.0088 ms |
| **10,000** | 9,999 | 0.6251 ms | 39 | 0.0110 ms |
| **100,000** | 99,999 | 7.8738 ms | 49 | 0.0081 ms |

### Conclusiones Preliminares:
- **Búsqueda Secuencial ($O(n)$):** Se observa un crecimiento estrictamente proporcional a $n$. Para 100.000 registros, el algoritmo debió recorrer prácticamente la totalidad de los elementos, reflejando el comportamiento lineal esperado.
- **Árbol Binario de Búsqueda ($O(\log n)$):** El número de nodos visitados se mantiene extremadamente bajo incluso al multiplicar por 100 el tamaño de los datos (apenas 49 pasos para 100.000 elementos), validando empíricamente la eficiencia de la división binaria del espacio de búsqueda.