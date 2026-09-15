📚 BookMatch 📚

Proyecto Integrador — Estructuras de Datos (UNaB) 
Comisión: 2 — Ing. Maximiliano Zorzoli  
Integrante: María Eugenia Abdo y Rossi  

Descripción del Proyecto
BookMatch es un sistema de recomendación y gestión de libros orientado a lectores apasionados de géneros específicos (como el *Thriller psicológico*). Su objetivo principal es resolver la problemática de encontrar la siguiente lectura ideal a partir de los gustos previos del usuario, evitando catálogos desordenados.

Este repositorio corresponde al TP 01, enfocado en la implementación de la arquitectura modular, programación orientada a objetos con encapsulamiento, carga de datos mediante archivos estructurados y operaciones básicas en terminal.

Estructura del Proyecto
El proyecto está organizado de forma modular para separar responsabilidades:

bookmatch/
│
├── Modelos/
│   └── libro.py        # Define la clase Libro con atributos encapsulados (@property)
│
├── Datos/
│   └── libros.json     # Base de datos local en formato JSON con los títulos de prueba
│
├── Servicios/
│   └── gestor.py       # Lógica de negocio (Carga de datos, Búsqueda, Listado y Filtrado)
│
├── main.py             # Interfaz de usuario por consola (Menú interactivo)
└── README.md           # Documentación del proyecto


INSTRUCCIONES DE EJECUCIÓN
