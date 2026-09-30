import time
import sys
from arbol_libros import ArbolBinarioBusqueda
from avl_arbol import ArbolAVL

# Aumentamos límite por seguridad en el BST
sys.setrecursionlimit(50000)

def comparar_rendimiento():
    print("=== TARJETA 3: COMPARATIVA EMPÍRICA (BST vs AVL con datos ordenados) ===")
    
    # Usaremos 3000 elementos para ver la diferencia abismal sin congelar la PC con el BST
    n = 3000
    titulos_ordenados = [f"Libro A_{i:05d}" for i in range(n)]
    
    print(f"\nProcesando dataset de {n} elementos ordenados alfabéticamente...")
    
    # 1. Prueba con BST Común
    print("\n--- 1. Árbol Binario de Búsqueda (BST Tradicional) ---")
    bst = ArbolBinarioBusqueda()
    inicio = time.time()
    for t in titulos_ordenados:
        bst.insertar(t, {"titulo": t})
    fin = time.time()
    tiempo_bst = fin - inicio
    print(f"⏱ Tiempo de inserción BST: {tiempo_bst:.6f} segundos")
    
    # 2. Prueba con Árbol AVL
    print("\n--- 2. Árbol AVL (Con balanceo automático) ---")
    avl = ArbolAVL()
    inicio = time.time()
    for t in titulos_ordenados:
        avl.insertar_titulo(t, {"titulo": t})
    fin = time.time()
    tiempo_avl = fin - inicio
    print(f"⏱ Tiempo de inserción AVL: {tiempo_avl:.6f} segundos")
    
    print(f"\n📊 Conclusión: El AVL procesó {n} elementos ordenados en una fracción del tiempo, evitando el desbalanceo.")

if __name__ == "__main__":
    comparar_rendimiento()