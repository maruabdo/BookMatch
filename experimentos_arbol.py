import json
import time
from arbol_libros import ArbolBinarioBusqueda

def cargar_catalogo_en_arbol(ruta_json):
    """Lee el archivo JSON del proyecto y carga los libros en el BST usando el título como clave."""
    arbol = ArbolBinarioBusqueda()
    
    try:
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            libros = json.load(archivo)
            
            for libro in libros:
                # Soportamos tanto 'title' como 'titulo' por si varía el JSON
                titulo = libro.get('title') or libro.get('titulo')
                if titulo:
                    arbol.insertar(titulo, libro)
                    
        print(f"-> Árbol cargado con éxito con los datos de {ruta_json}.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_json}.")
        
    return arbol

if __name__ == "__main__":
    archivos = ["libros_1000.json", "libros_10000.json", "libros_100000.json"]
    
    print("=== INICIANDO EXPERIMENTOS DE RENDIMIENTO (BST) ===")
    
    for archivo in archivos:
        print(f"\n--- Probando con: {archivo} ---")
        
        inicio_carga = time.time()
        arbol = cargar_catalogo_en_arbol(archivo)
        fin_carga = time.time()
        
        tiempo_carga = fin_carga - inicio_carga
        print(f"⏱️️ Tiempo de construcción: {tiempo_carga:.6f} segundos.")
        
        if arbol.raiz:
            titulo_prueba = "Libro de Prueba 1" # O el título que sepas que está en esos JSON
            
            inicio_busq = time.time()
            encontrado = arbol.buscar(titulo_prueba)
            fin_busq = time.time()
            
            tiempo_busq = fin_busq - inicio_busq
            estado = "Encontrado" if encontrado else "No encontrado"
            print(f"🔍 Búsqueda: {estado} en {tiempo_busq:.8f} segundos.")

    print("\n=== EXPERIMENTOS FINALIZADOS ===")