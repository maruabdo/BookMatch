import json
import os
from Modelos.libro import Libro

class GestorLibros:
    def __init__(self, ruta_archivo="datos/libros.json"):
        self._libros = []
        self._cargar_datos(ruta_archivo)
        
    def _cargar_datos(self, ruta):
        if os.path.exists(ruta):
            with open(ruta, 'r', encoding='utf-8') as archivo:
                datos_json = json.load(archivo)
                for item in datos_json:
                    un_libro = Libro(
                        isbn=item.get("isbn"),
                        titulo=item.get("titulo"),
                        autor=item.get("autor"),
                        genero=item.get("genero"),
                        rating=item.get("rating")
                    )
                    self._libros.append(un_libro)
        else:
            print(f"⚠️ El archivo {ruta} no existe")
            
    def listar_libros(self):
        return self._libros
    
    def buscar_por_titulo(self, titulo_buscado):
        for libro in self._libros:
            if titulo_buscado.lower() in libro.titulo.lower():
                return libro
        return None
    
    def filtrar_por_genero(self, genero_buscado):
        resultados = []
        for libro in self._libros:
            if genero_buscado.lower() == libro.genero.lower():
                resultados.append(libro)
        return resultados
    
    