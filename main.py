from Servicios.gestor import GestorLibros

def mostrar_menu():
    print("\n" + "=" * 45)
    print("             📚 BOOKMATCH — TERMINAL")
    print("=" * 45)
    print("1. Listar todos los libros")
    print("2. Buscar libro por título")
    print("3. Filtrar libros por género")
    print("0. Salir")
    print("-" * 45)
    
def main():
    gestor = GestorLibros()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- 📖 LISTADO COMPLETO DE LIBROS ---")
            libros = gestor.listar_libros()
        
            if libros:
                for libro in libros:
                    print(f"  • {libro}")
            else:
                print(" ‼️ No hay libros cargados en el sistema.")
        
        elif opcion == "2":
            print("\n--- 🔍 BÚSQUEDA DE LIBRO ---")
            titulo_ingresado = input("Ingrese el título a buscar: ")
            libro_encontrado = gestor.buscar_por_titulo(titulo_ingresado)

            if libro_encontrado:
                print(f"\n  ✅ ¡Libro encontrado!")
                print(f"  > {libro_encontrado}")
            else:
                print(
                    f"\n  ❌ No se encontró ningún libro con el título"
                    f" '{titulo_ingresado}'."
                )
                
        elif opcion == "3":
            print("\n--- 🎭 FILTRAR POR GÉNERO ---")
            genero_ingresado = input("Ingrese el género (ej: Thriller psicológico): ")
            resultados = gestor.filtrar_por_genero(genero_ingresado)

            if resultados:
                print(f"\n  📚 Libros encontrados en '{genero_ingresado}':")
                for libro in resultados:
                    print(f"  • {libro}")
            else:
                print(f"\n  ❌ No hay libros para el género '{genero_ingresado}'.")

        elif opcion == "0":
            print("\n¡Gracias por usar BookMatch! Saliendo del sistema... 📚✨")
        
            break
    
        else:
            print("\n ⚠️ Opción inválida. Por favor, elija un número del 0 al 3.")
            
if __name__ == "__main__":
    main()