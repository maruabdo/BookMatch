# Informe TP 2: Complejidad y Análisis de Rendimiento - BookMatch

## 1. Definición de la Operación Crítica
* **Operación elegida:** Búsqueda de libros por título (`buscar_por_titulo`).
* **Justificación técnica:** Se selecciona esta operación por ser la consulta más frecuente e importante para el usuario del sistema. Con un volumen pequeño de datos (como 20 elementos), una búsqueda secuencial es imperceptible; sin embargo, al escalar el sistema a 100.000 elementos, el tiempo de respuesta lineal se degrada de forma significativa ($O(n)$). Esto hace necesario e indispensable evaluar y comparar una estructura jerárquica basada en árboles para optimizar los tiempos de acceso.