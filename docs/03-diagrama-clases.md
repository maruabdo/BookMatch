# Diagrama de Clases y Componentes — BookMatch

## Clases Principales del Dominio y Servicios (V1)

El sistema está diseñado bajo el paradigma de Programación Orientada a Objetos (POO), separando el modelo de datos, la lógica de negocio y la interfaz de usuario.

```text

+-------------------+             +-----------------------+
|      Libro        |             |     GestorLibros      |
+-------------------+             +-----------------------+
| - _isbn: str      |             | - libros: list        |
| - _titulo: str    |             +-----------------------+
| - _autor: str     |             | + cargar_datos()      |
| - _genero: str    |             | + listar_libros()     |
| - _rating: float  |             | + buscar_por_titulo() |
+-------------------+             | + filtrar_por_genero()|
| + titulo (prop)   |             +-----------------------+
| + __repr__()      |                         │
+-------------------+                         │ usa
         ▲                                    ▼
         │                                    │
         └───────────────────────── [ Archivo libros.json ]

```

## Relaciones y Responsabilidades

Libro (Modelos/libro.py): Representa la entidad de dominio. Implementa atributos protegidos y utiliza el decorador @property para un acceso seguro y encapsulado.
GestorLibros (Servicios/gestor.py): Contiene la lógica de negocio. Se encarga de levantar la información desde el archivo JSON, instanciar los objetos y ejecutar las operaciones de filtrado y búsqueda.
main.py: Actúa como controlador de la interfaz de terminal, capturando las opciones del usuario y llamando a los métodos del servicio.

