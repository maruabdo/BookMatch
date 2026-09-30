class NodoAVL:
    def __init__(self, titulo, datos=None):
        self.titulo = titulo
        self.datos = datos if datos is not None else {}
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _obtener_factor_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha)

    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))
        x.altura = 1 + max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha))

        return x

    def _rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))

        return y

    def _insertar(self, nodo, titulo, datos):
        if not nodo:
            return NodoAVL(titulo, datos)

        if titulo < nodo.titulo:
            nodo.izquierda = self._insertar(nodo.izquierda, titulo, datos)
        elif titulo > nodo.titulo:
            nodo.derecha = self._insertar(nodo.derecha, titulo, datos)
        else:
            return nodo

        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))

        balance = self._obtener_factor_balance(nodo)

        # Rotaciones
        # Izquierda-Izquierda
        if balance > 1 and titulo < nodo.izquierda.titulo:
            return self._rotar_derecha(nodo)

        # Derecha-Derecha
        if balance < -1 and titulo > nodo.derecha.titulo:
            return self._rotar_izquierda(nodo)

        # Izquierda-Derecha
        if balance > 1 and titulo > nodo.izquierda.titulo:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        # Derecha-Izquierda
        if balance < -1 and titulo < nodo.derecha.titulo:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def insertar_titulo(self, titulo, datos=None):
        self.raiz = self._insertar(self.raiz, titulo, datos)