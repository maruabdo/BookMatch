# Gestión del Proyecto (Tablero y Metodología) — BookMatch

## Metodología de Trabajo (Scrum Simplificado)
Para el desarrollo del proyecto se implementa un enfoque ágil adaptado a los Sprints de la materia (un Sprint por cada entrega de TP). 
- **Tablero de gestión:** Se utiliza una herramienta de visualización (Tablero Kanban digital) estructurado con las siguientes columnas mínimas: 
  - *Backlog* (Tareas pendientes o futuras etapas)
  - *En progreso* (Tareas activas del TP actual)
  - *En revisión* (Pruebas de código y validación de requerimientos)
  - *Hecho* (Funcionalidades probadas y mergeadas a la rama principal)

---

## Historias de Usuario (Sprint 1 / TP 1)

### HU01 — Carga y Listado de Catálogo
- **Como** lector apasionado por el thriller psicológico,
- **Quiero** que el sistema cargue un catálogo inicial y me permita listar todos los libros disponibles,
- **Para** poder ver rápidamente qué opciones tengo para leer.
- **Criterios de aceptación:**
  - El sistema lee los datos de un archivo `libros.json`.
  - Muestra todos los registros formateados correctamente en consola.
  - Responde de forma inmediata sin errores de lectura.

### HU02 — Búsqueda y Filtrado
- **Como** usuario del sistema,
- **Quiero** buscar libros por título y filtrarlos por género,
- **Para** encontrar lecturas específicas sin tener que revisar todo el listado manual.
- **Criterios de aceptación:**
  - Permite ingresar cadenas de texto para buscar coincidencias en los títulos.
  - Permite filtrar el catálogo devolviendo únicamente los libros del género seleccionado.

## Tablero de Trello
- **Enlace al tablero:** https://trello.com/invite/b/6aaa967471e6dd0e61bb6c31/ATTI15f9e23aac28f47e0982efbc40b9294c56EAEFEF/bookmatch