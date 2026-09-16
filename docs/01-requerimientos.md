# Requerimientos del Proyecto — BookMatch

## Requerimientos Funcionales (RF)
- **RF01 — Carga inicial de datos:** El sistema debe cargar automáticamente el catálogo de libros desde un archivo estructurado en formato JSON al iniciar la ejecución.
- **RF02 — Listar catálogo:** El sistema debe permitir al usuario visualizar la lista completa de libros disponibles en el sistema con sus datos principales.
- **RF03 — Buscar por título:** El sistema debe permitir buscar libros ingresando un título (o fragmento de este) y retornar las coincidencias encontradas.
- **RF04 — Filtrar por género:** El sistema debe permitir filtrar el catálogo para mostrar únicamente los libros que correspondan a un género específico (ej: thriller psicológico).

## Requerimientos No Funcionales (RNF)
- **RNF01 — Paradigma y Encapsulamiento:** El código fuente debe estar desarrollado en Python utilizando Programación Orientada a Objetos (POO), aplicando atributos protegidos y getters mediante el decorador `@property`.
- **RNF02 — Arquitectura Modular:** El proyecto debe estructurarse de manera modular separando responsabilidades (Modelos, Datos, Servicios y Interfaz de Terminal).
- **RNF03 — Consola Interactiva:** La interfaz de usuario debe operar mediante la terminal de forma clara, amigable y guiada por menús numéricos.

## Alcance y Fuera de Alcance
- **En alcance (V1):** Gestión local de datos mediante JSON, operaciones básicas (listar, buscar, filtrar), arquitectura orientada a objetos en Python y documentación estándar de desarrollo.
- **Fuera de alcance:** Autenticación y gestión de múltiples usuarios, interfaces gráficas de escritorio o web, y persistencia en bases de datos relacionales avanzadas (estas características se evaluarán en etapas posteriores de la cursada).