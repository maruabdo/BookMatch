# 📚 BookMatch

¡Hola! Este es mi proyecto integrador para la materia **Estructura de Datos** de la UNaB (Comisión 2, con el Ing. Zorzoli). 

## 👥 Integrantes
- **María Eugenia Abdo y Rossi** 

---

## 💡 ¿De qué trata el proyecto?
BookMatch surge como un sistema de gestión y recomendación de libros pensado para lectores apasionados por géneros específicos, como el thriller psicológico. La idea principal es resolver la dificultad de encontrar lecturas afines mediante un catálogo ordenado y accesible. 
En esta primera versión (TP 1), el proyecto se enfoca en implementar la arquitectura base en Python utilizando Programación Orientada a Objetos (POO), encapsulamiento, carga de datos estructurados desde un archivo JSON y operaciones básicas interactivas por consola.

---

## 📂 Estructura del proyecto
Organicé el código de forma modular para que quede prolijo y respete las buenas prácticas de arquitectura:
- `Modelos/`: Acá vive la clase `Libro` con sus respectivos atributos protegidos y getters.
- `Datos/`: Guarda el archivo `libros.json` con la información inicial de prueba.
- `Servicios/`: Contiene la lógica del gestor que procesa los datos y arma las operaciones de búsqueda y filtrado.
- `main.py`: Es la interfaz de terminal interactiva para correr el programa.

---

## 🧪 Datos de prueba
Para probar que todo funcione bien, dejé cargado un archivo `libros.json` en la carpeta `Datos/` con algunas novelas de prueba (como *La asistenta*, *La paciente silenciosa*, entre otras) que incluyen su ISBN, título, autor, género y rating.

---

## 🚀 ¿Cómo ejecutarlo?
Si querés probar el programa en tu compu, seguí estos pasos sencillos desde la terminal:

1. Cloná o descargá este repositorio.
2. Parate en la carpeta principal del proyecto (`BookMatch`):
    ```bash
    cd ruta/a/tu/carpeta/BookMatch
    ```
3. Ejecutá el archivo principal con: 
    ```bash
    python3 main.py
    ```

---

## 🖥️ Demo de la V1
Al ejecutar el script, se abre un menú en la consola que permite hacer las tres operaciones obligatorias del TP1:
* Listar todos los libros: Muestra el catálogo completo disponible.
* Buscar por título: Permite ingresar el nombre de un libro para encontrarlo rápido.
* Filtrar por género: Muestra una lista filtrada con los títulos que coincidan con el género ingresado.

---

## 📄 Documentación del Proyecto
Toda la documentación formal correspondiente al TP 1 se encuentra en la carpeta `docs/`:
- [01 - Requerimientos](docs/01-requerimientos.md)
- [02 - Casos de Uso](docs/02-casos-de-uso.md)
- [03 - Diagrama de Clases](docs/03-diagrama-clases.md)
- [04 - Diagrama de Datos](docs/04-diagrama-datos.md)
- [05 - Gestión del Proyecto (Trello)](docs/05-gestion-proyecto.md)