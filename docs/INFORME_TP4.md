# Informe Técnico: TP4 - Árboles AVL y Desbalanceo

**Autor:** María Eugenia Abdo y Rossi
**Grupo:** 32  
**Repositorio:** BookMatch (`feature/tp4-avl`)  

---

## 1. Introducción y Objetivos
El objetivo principal de este trabajo práctico es investigar el comportamiento de los Árboles Binarios de Búsqueda (BST) tradicionales ante escenarios de desbalanceo severo (peor caso al insertar claves ordenadas), y demostrar cómo el uso de **Árboles AVL** con rotaciones automáticas preserva la complejidad óptima de búsqueda en $O(\log n)$.

---

## 2. Tarjeta 1: El Desafío del Desbalance (BST Común)
Cuando se insertan claves estrictamente ordenadas alfabéticamente en un BST convencional, la estructura pierde su factor de balance y se degenera en una lista enlazada unidireccional (altura $O(n)$). 

### Evidencia empírica obtenida:
* **Dataset de 1.000 elementos ordenados:**
  * Tiempo de inserción: `0.0258 s`
  * Tiempo de búsqueda (peor caso): `0.000054 s`
* **Dataset de 3.000 elementos ordenados:**
  * Tiempo de inserción: `0.2699 s`
  * Tiempo de búsqueda (peor caso): `0.000153 s`
* **Dataset de 5.000 elementos ordenados:**
  * Tiempo de inserción: `0.5792 s`
  * Tiempo de búsqueda (peor caso): `0.000226 s`

*Conclusión parcial:* El crecimiento del tiempo de inserción no es lineal, evidenciando la penalización por la degradación estructural del árbol.

---

## 3. Tarjeta 2: Implementación del Árbol AVL
Se desarrolló el módulo `avl_arbol.py`, incorporando:
* Control estricto de altura por nodo.
* Cálculo automático del factor de balance ($h_{izq} - h_{der}$).
* Implementación de las cuatro rotaciones fundamentales:
  1. Rotación Simple a la Derecha ($LL$).
  2. Rotación Simple a la Izquierda ($RR$).
  3. Rotación Doble Izquierda-Derecha ($LR$).
  4. Rotación Doble Derecha-Izquierda ($RL$).

---

## 4. Tarjeta 3: Experimentos Comparativos (BST vs. AVL)
Para contrastar el rendimiento, se alimentó tanto al BST tradicional como al Árbol AVL con un dataset de **3.000 títulos ordenados alfabéticamente** (peor caso absoluto).

### Resultados de la comparativa:
* **Tiempo de inserción (BST Tradicional):** `0.293246 segundos`
* **Tiempo de inserción (Árbol AVL):** `0.012689 segundos`

> **Análisis:** El Árbol AVL procesó el dataset ordenado en una fracción del tiempo (más de 20 veces más rápido que el BST), aplicando balanceo automático y evitando por completo la degradación de altura.

---

## 5. Conclusión Técnica
El balanceo automático en los Árboles AVL mediante rotaciones garantiza que la altura se mantenga acotada en $O(\log n)$, evitando el colapso operativo que sufren los BST tradicionales ante catálogos o entradas preordenadas. Esto asegura un rendimiento predecible, escalable y robusto para sistemas de indexación de alta exigencia como *BookMatch*.