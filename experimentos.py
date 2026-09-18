import json
import time
from busquedas import busqueda_secuencial, ArbolBinarioBusqueda

def medir_rendimiento(nombre_archivo, titulo_a_buscar):
    """
    Función cliente que carga el dataset, puebla las estructuras y 
    compara el rendimiento temporal y de pasos lógicos de ambas estrategias.
    """
    print(f"\n--------------------------------------------------")
    print(f"Analizando dataset: {nombre_archivo}")
    print(f"--------------------------------------------------")

    # 1. Carga de datos
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            libros = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}. Corré el generador primero.")
        return

    n = len(libros)
    print(f"Registros en memoria (n = {n:,})")

    # ==========================================
    # MEDICIÓN 1: Búsqueda Secuencial O(n)
    # ==========================================
    inicio = time.time()
    _, pasos_secuencial = busqueda_secuencial(libros, titulo_a_buscar)
    fin = time.time()
    tiempo_secuencial = (fin - inicio) * 1000  # Convertimos a milisegundos

    print(f"-> [Secuencial] Pasos lógicos: {pasos_secuencial:,} | Tiempo: {tiempo_secuencial:.4f} ms")

    # ==========================================
    # MEDICIÓN 2: Árbol Binario de Búsqueda O(log n)
    # ==========================================
    arbol = ArbolBinarioBusqueda()
    for libro in libros:
        arbol.insertar(libro["titulo"], libro)

    inicio = time.time()
    _, pasos_bst = arbol.buscar(titulo_a_buscar)
    fin = time.time()
    tiempo_bst = (fin - inicio) * 1000  # Convertimos a milisegundos

    print(f"-> [BST]        Pasos lógicos: {pasos_bst:,} | Tiempo: {tiempo_bst:.4f} ms")


if __name__ == "__main__":
    print("=== INICIANDO EXPERIMENTOS DE RENDIMIENTO (TP2) ===")
    
    # Buscamos un elemento en el peor caso (al final de los datasets)
    titulo_objetivo = "Libro de Prueba 99999" 
    
    medir_rendimiento("libros_1000.json", "Libro de Prueba 999")
    medir_rendimiento("libros_10000.json", "Libro de Prueba 9999")
    medir_rendimiento("libros_100000.json", titulo_objetivo)