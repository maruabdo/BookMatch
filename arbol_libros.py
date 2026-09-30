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
                
    def buscar(self, titulo):
        """Busca un libro por su título en el árbol de forma eficiente."""
        return self._buscar_recursivo(self.raiz, titulo)

    def _buscar_recursivo(self, nodo_actual, titulo):
        # Caso base: si el nodo es nulo o encontramos el título
        if nodo_actual is None or nodo_actual.titulo == titulo:
            return nodo_actual
        
        # Si el título buscado es menor, vamos a la izquierda
        if titulo < nodo_actual.titulo:
            return self._buscar_recursivo(nodo_actual.izquierdo, titulo)
        
        # Si es mayor, vamos a la derecha
        return self._buscar_recursivo(nodo_actual.derecho, titulo)

    def inorder(self, nodo, resultado=None):
        """Recorrido In-Order (Izquierda, Raíz, Derecha). 
        Devuelve el catálogo ordenado alfabéticamente."""
        if resultado is None:
            resultado = []
        if nodo is not None:
            self.inorder(nodo.izquierdo, resultado)
            resultado.append(nodo.titulo)
            self.inorder(nodo.derecho, resultado)
        return resultado
    


# Chequeo
if __name__ == "__main__":
    # Creamos una instancia del árbol
    arbol = ArbolBinarioBusqueda()
    
    # Insertamos algunos libros de prueba
    arbol.insertar("Rayuela", {"autor": "Julio Cortázar", "año": 1963})
    arbol.insertar("El Principito", {"autor": "Antoine de Saint-Exupéry", "año": 1943})
    arbol.insertar("Ficciones", {"autor": "Jorge Luis Borges", "año": 1944})
    
    # Probamos el recorrido Inorder (debe mostrar los títulos ordenados alfabéticamente)
    print("--- Recorrido Inorder (Ordenado) ---")
    print(arbol.inorder(arbol.raiz))
    
    # Probamos la búsqueda
    print("\n--- Probando Búsqueda ---")
    libro_buscado = "Ficciones"
    resultado = arbol.buscar(libro_buscado)
    if resultado:
        print(f"¡Encontrado! -> Título: {resultado.titulo}, Autor: {resultado.datos['autor']}")
    else:
        print(f"El libro '{libro_buscado}' no fue encontrado.")