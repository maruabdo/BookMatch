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
    # Probamos con el archivo de 1000 libros para empezar
    ruta_archivo = "libros_1000.json" 
    print(f"Cargando {ruta_archivo} en el BST...")
    
    inicio_carga = time.time()
    arbol_libros = cargar_catalogo_en_arbol(ruta_archivo)
    fin_carga = time.time()
    
    print(f"Tiempo de construcción del árbol: {fin_carga - inicio_carga:.6f} segundos.")
    
    # Probamos el tiempo de búsqueda en el árbol
    if arbol_libros.raiz:
        titulo_a_buscar = "Libro de Prueba 1"
        print(f"\nBuscando el libro: '{titulo_a_buscar}'...")
        
        inicio_busqueda = time.time()
        resultado = arbol_libros.buscar(titulo_a_buscar)
        fin_busqueda = time.time()
        
        if resultado:
            print(f"¡Encontrado! Título: {resultado.titulo}")
        else:
            print("El libro no se encuentra en el árbol.")
            
        print(f"Tiempo de búsqueda en BST: {fin_busqueda - inicio_busqueda:.6f} segundos.")