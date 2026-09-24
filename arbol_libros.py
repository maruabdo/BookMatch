class NodoLibro:
    def __init__(self, titulo, datos_libro):
        self.titulo = titulo          # La clave que ordena el árbol
        self.datos = datos_libro      # El resto de la info del libro (autor, año, etc.)
        self.izquierdo = None         # Puntero al subárbol izquierdo (menores)
        self.derecho = None           # Puntero al subárbol derecho (mayores)

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None              # El árbol arranca vacío

    def insertar(self, titulo, datos_libro):
        """Inserta un nuevo libro en el árbol manteniendo el orden alfabético por título."""
        nuevo_nodo = NodoLibro(titulo, datos_libro)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        # Comparamos alfabéticamente los títulos
        if nuevo_nodo.titulo < nodo_actual.titulo:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecho, nuevo_nodo)