# ==========================================
# ESTRATEGIA 1: BÚSQUEDA SECUENCIAL (Lineal)
# ==========================================
def busqueda_secuencial(libros, titulo_buscado):
    """
    Realiza una búsqueda lineal sobre una lista desordenada de libros.
    Basado en los fundamentos de algoritmos de Goodrich et al. y Aho et al.
    
    Precondiciones: 
        - 'libros' debe ser una lista válida de diccionarios con la clave 'titulo'.
        - 'titulo_buscado' debe ser un string no vacío.
    Postcondiciones: 
        - Retorna una tupla (libro_encontrado, pasos) donde libro_encontrado es el diccionario 
          o None si no existe, y 'pasos' es la cantidad de comparaciones realizadas.
    Complejidad temporal: 
        - O(n), donde n es el tamaño de la lista (recorrido lineal completo en el peor caso).
    """
    pasos = 0
    for libro in libros:
        pasos += 1  # Conteo de operación elemental (comparación)
        if libro["titulo"].lower() == titulo_buscado.lower():
            return libro, pasos
    return None, pasos


# ==========================================
# ESTRATEGIA 2: ÁRBOL BINARIO DE BÚSQUEDA (BST)
# ==========================================
class NodoBST:
    """Representa un nodo individual dentro del Árbol Binario de Búsqueda."""
    def __init__(self, titulo, datos):
        self.titulo = titulo      # Clave de ordenamiento (Key)
        self.datos = datos        # Valor asociado (Value / Diccionario del libro)
        self.izq = None           # Subárbol izquierdo (menores)
        self.der = None           # Subárbol derecho (mayores)


class ArbolBinarioBusqueda:
    """
    Estructura jerárquica de Árbol Binario de Búsqueda (BST).
    Mantiene la propiedad de orden en las claves para optimizar búsquedas O(log n),
    siguiendo el estándar bibliográfico de la cátedra.
    """
    def __init__(self):
        self.raiz = None

    def insertar(self, titulo, datos):
        """Inserta un nuevo nodo manteniendo la invariante del BST."""
        if self.raiz is None:
            self.raiz = NodoBST(titulo, datos)
        else:
            self._insertar_recursivo(self.raiz, titulo, datos)

    def _insertar_recursivo(self, nodo_actual, titulo, datos):
        if titulo.lower() < nodo_actual.titulo.lower():
            if nodo_actual.izq is None:
                nodo_actual.izq = NodoBST(titulo, datos)
            else:
                self._insertar_recursivo(nodo_actual.izq, titulo, datos)
        elif titulo.lower() > nodo_actual.titulo.lower():
            if nodo_actual.der is None:
                nodo_actual.der = NodoBST(titulo, datos)
            else:
                self._insertar_recursivo(nodo_actual.der, titulo, datos)

    def buscar(self, titulo_buscado):
        """
        Busca un libro utilizando división binaria del espacio de búsqueda.
        
        Precondiciones: El árbol debe estar construido e inicializado correctamente.
        Postcondiciones: Retorna una tupla (nodo_encontrado, pasos) indicando el nodo 
                         y la cantidad de nodos visitados durante el recorrido.
        Complejidad temporal: 
            - O(log n) en promedio (árbol balanceado).
            - O(n) en el peor caso (árbol degenerado).
        """
        return self._buscar_recursivo(self.raiz, titulo_buscado, pasos=0)

    def _buscar_recursivo(self, nodo_actual, titulo_buscado, pasos):
        if nodo_actual is None:
            return None, pasos

        pasos += 1  # Conteo de nodo visitado
        if nodo_actual.titulo.lower() == titulo_buscado.lower():
            return nodo_actual, pasos

        if titulo_buscado.lower() < nodo_actual.titulo.lower():
            return self._buscar_recursivo(nodo_actual.izq, titulo_buscado, pasos)
        
        return self._buscar_recursivo(nodo_actual.der, titulo_buscado, pasos)