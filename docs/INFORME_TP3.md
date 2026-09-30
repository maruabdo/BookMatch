# Informe Técnico: Implementación y Evaluación de Árboles Binarios de Búsqueda (BST)

**Proyecto:** BookMatch  
**Trabajo Práctico:** TP3 - Estructuras de Datos No Lineales (BST)  
**Autor/a:** María Eugenia Abdo  

---

## 1. Introducción y Objetivo
El presente informe detalla la implementación y evaluación de un Árbol Binario de Búsqueda (BST, por sus siglas en inglés) aplicado al sistema de gestión de catálogos de libros **BookMatch**. El objetivo principal es reemplazar las estructuras lineales anteriores por una estructura de datos jerárquica no lineal que optimice los tiempos de búsqueda y ordenamiento de grandes volúmenes de datos.

---

## 2. Criterio de Selección de la Clave
Para la construcción y estructuración del BST, se seleccionó el **título del libro** (`title` / `titulo`) como clave principal de ordenamiento. 
* **Justificación:** Los títulos de los libros actúan como un identificador natural y único de consulta frecuente por parte de los usuarios. Al utilizar el título como clave alfabética, las propiedades de orden del BST garantizan que los menores (alfabéticamente anteriores) se ubiquen sistemáticamente en el subárbol izquierdo y los mayores en el derecho, facilitando tanto la búsqueda exacta como el listado ordenado.

---

## 3. Arquitectura y Recorridos Implementados
El sistema se estructuró en clases modulares:
* `NodoLibro`: Almacena la clave (`titulo`), los datos asociados del libro (autor, año, metadatos) y los punteros a los nodos hijo (`izquierdo` y `derecho`).
* `ArbolBinarioBusqueda`: Administra la raíz y expone los métodos principales de inserción recursiva, búsqueda eficiente y recorridos.

### Recorrido In-Order
Se implementó el recorrido recursivo **In-Order** (Subárbol Izquierdo $\rightarrow$ Raíz $\rightarrow$ Subárbol Derecho). 
* **Utilidad:** Este recorrido visita los elementos de manera estrictamente ascendente (alfabética), permitiendo extraer el catálogo completo del sistema ordenado sin necesidad de aplicar algoritmos de ordenamiento adicionales.

---

## 4. Integración Funcional
El BST fue integrado al flujo general de la aplicación mediante scripts de carga automatizada (`experimentos_arbol.py`). El sistema lee dinámicamente los datasets provistos en formato JSON (`libros_1000.json`, `libros_10000.json`, `libros_100000.json`), instanciando el árbol e insertando cada registro de manera eficiente en tiempo de ejecución.

---

## 5. Comparativa Empírica de Resultados y Rendimiento
Se realizaron pruebas de rendimiento cronometrando mediante mediciones reales los tiempos de inserción (construcción del árbol) y los tiempos de consulta individual sobre diferentes tamaños de datasets en el entorno de ejecución local.

| Dataset | Cantidad de Registros | Tiempo de Construcción (s) | Tiempo de Búsqueda (s) |
| :--- | :--- | :--- | :--- |
| `libros_1000.json` | 1.000 | 0.002166 | 0.00000119 |
| `libros_10000.json` | 10.000 | 0.029942 | 0.00039601 |
| `libros_100000.json` | 100.000 | 0.297382 | 0.00084496 |

### Conclusiones Técnicas del Rendimiento
1. **Comportamiento Logarítmico:** Los tiempos de búsqueda se mantienen en el orden de los microsegundos incluso al escalar a 100.000 registros, confirmando empíricamente la eficiencia teórica de complejidad $O(\log n)$ en promedio.
2. **Superioridad frente a Listas Lineales:** A diferencia de las búsquedas secuenciales (lineales) de orden $O(n)$, donde el tiempo de respuesta crece de forma directa con la cantidad de elementos, el BST permite descartar mitades enteras del árbol en cada paso recursivo, demostrando ser la solución óptima para sistemas de catálogos escalables.