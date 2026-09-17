import json
import random

def generar_dataset(cantidad):
    autores = ["Stephen King", "John Katzenbach", "Paula Hawkins", "Freida McFadden", "Alex Michaelides", "Harlan Coben", "Shari Lapena", "Gillian Flynn"]
    generos = ["Thriller psicológico", "Suspenso", "Novela negra", "Misterio", "Terror"]

    libros = []
    for i in range(1, cantidad + 1):
        libro = {
            "isbn": f"978-987-{random.randint(1000, 9999)}-{random.randint(10, 99)}-{random.randint(0, 9)}",
            "titulo": f"Libro de Prueba {i}",
            "autor": random.choice(autores),
            "genero": random.choice(generos),
            "rating": round(random.uniform(3.0, 5.0), 1)
        }
        libros.append(libro)

    nombre_archivo = f"libros_{cantidad}.json"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=4)

    print(f"¡Dataset de {cantidad:,} libros generado con éxito en '{nombre_archivo}'!")

if __name__ == "__main__":
    print("Generando datasets de prueba para TP2...")
    generar_dataset(1000)
    generar_dataset(10000)
    generar_dataset(100000)
    print("¡Proceso finalizado!")