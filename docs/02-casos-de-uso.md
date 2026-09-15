# Casos de Uso — BookMatch (Versión 1)

## Diagrama Conceptual de Casos de Uso
*(Representación textual del flujo de interacción del usuario con el sistema)*

---

### Caso de Uso 01: Listar Catálogo Completo
- **Actor:** Usuario / Lector
- **Precondición:** El archivo `libros.json` está correctamente ubicado y cargado en memoria.
- **Flujo Principal:**
  1. El usuario selecciona la opción "Listar todos los libros" en el menú de la consola.
  2. El sistema recorre los objetos del catálogo en memoria.
  3. El sistema muestra por pantalla el listado completo de títulos, autores, géneros y ratings.
- **Flujo Alternativo:** Si el catálogo está vacío, el sistema notifica que no hay libros registrados.

---

### Caso de Uso 02: Buscar Libro por Título
- **Actor:** Usuario / Lector
- **Precondición:** El catálogo de libros está cargado.
- **Flujo Principal:**
  1. El usuario selecciona la opción "Buscar por título".
  2. El sistema solicita el ingreso del título o palabra clave.
  3. El usuario ingresa el texto de búsqueda.
  4. El sistema procesa la consulta y devuelve los libros que coincidan total o parcialmente.
- **Flujo Alternativo:** Si no se encuentran coincidencias, el sistema informa que el libro no está disponible.

---

### Caso de Uso 03: Filtrar por Género
- **Actor:** Usuario / Lector
- **Precondición:** El catálogo de libros cuenta con registros clasificados por género.
- **Flujo Principal:**
  1. El usuario selecciona la opción "Filtrar por género".
  2. El sistema solicita especificar el género deseado (ej: *Thriller psicológico*).
  3. El usuario ingresa el género.
  4. El sistema filtra y despliega en consola los libros que pertenecen a dicha categoría.