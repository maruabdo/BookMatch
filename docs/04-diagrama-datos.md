# Diagrama de Conexión entre Estructuras de Datos — BookMatch

Este diagrama describe cómo fluyen los datos a través del sistema en esta primera versión y cómo se preparan las bases para futuras estructuras más avanzadas:

```text
   [ Archivo JSON (Datos/libros.json) ]
                    │
                    ▼ (Lectura y parseo al iniciar)
         [ Lista de Objetos Libro ]
                    │
                    ▼ (Operaciones del Gestor / Servicios)
       ┌────────────┴────────────┐
       ▼                         ▼
  [ Búsqueda lineal ]     [ Filtrado por género ]
  (Búsqueda por título)   (Subconjunto de objetos)
       │                         │
       └────────────┬────────────┘
                    ▼
          [ Interfaz de Terminal ]
                    │
                    ▼
          (Visualización al Usuario)

