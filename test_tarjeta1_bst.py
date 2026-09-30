import time
import sys
from arbol_libros import ArbolBinarioBusqueda

# Aumentamos temporalmente el límite de recursión por seguridad ante el desbalanceo severo
sys.setrecursionlimit(50000)

def probar_degradacion_bst():
    print("=== TARJETA 1: EVIDENCIA DE DEGRADACIÓN EN BST COMÚN ===")
    
    # Datasets de prueba con claves estrictamente ordenadas alfabéticamente
    tamanios = [1000, 3000, 5000]
    
    for n in tamanios:
        titulos_ordenados = [f"Libro A_{i:05d}" for i in range(n)]
        
        bst = ArbolBinarioBusqueda()
        
        # 1. Inserción con datos ordenados (peor caso para un BST común)
        inicio = time.time()
        for t in titulos_ordenados:
            bst.insertar(t, {"titulo": t})
        fin = time.time()
        tiempo_insercion = fin - inicio
        
        # 2. Búsqueda del último elemento (el nodo más profundo, peor caso absoluto)
        elemento_a_buscar = titulos_ordenados[-1]
        inicio_busq = time.time()
        bst.buscar(elemento_a_buscar)
        fin_busq = time.time()
        tiempo_busqueda = fin_busq - inicio_busq
        
        print(f"\n[Dataset de {n} elementos ordenados]")
        print(f"-> Tiempo de inserción: {tiempo_insercion:.6f} segundos")
        print(f"-> Tiempo de búsqueda (peor caso): {tiempo_busqueda:.8f} segundos")
        print(f"⚠️ Evidencia: El BST se degeneró estructuralmente a altura O(n).")

if __name__ == "__main__":
    probar_degradacion_bst()
    