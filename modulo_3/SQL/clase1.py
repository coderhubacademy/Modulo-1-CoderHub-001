# Clase SQL

# Que es SQL?

# SQL (Structured Query Language) es un lenguaje de programación 
# utilizado para gestionar y manipular bases de datos relacionales.
# # SQL permite realizar operaciones como crear, leer, actualizar y eliminar
# datos en una base de datos.
# # SQL es un lenguaje declarativo, lo que significa que se centra en
# describir qué se quiere hacer con los datos, en lugar de cómo hacerlo.
# # SQL es un lenguaje estándar utilizado por muchos sistemas de gestión
# de bases de datos, como MySQL, PostgreSQL, Oracle y Microsoft SQL Server o SQLite.

# Que es SQLite?

# SQLite es un sistema de gestión de bases de datos relacional ligero y
# autónomo. Es una biblioteca escrita en C que proporciona una base de datos
# SQL integrada. SQLite es ampliamente utilizado debido a su simplicidad,
# portabilidad y facilidad de uso. No requiere un servidor separado para
# funcionar, lo que lo hace ideal para aplicaciones pequeñas y medianas,
# así como para aplicaciones móviles y de escritorio. SQLite almacena
# todos los datos en un solo archivo, lo que facilita la gestión y
# distribución de la base de datos. Además, es compatible con la mayoría
# de los estándares SQL, lo que permite realizar consultas y operaciones
# de bases de datos de manera similar a otros sistemas de gestión de bases
# de datos más grandes.

# Entidades
# Tipos de entidades
# Relaciones entre entidades
# Tipos de relaciones entre entidades

# Bases de datos
# Base de datos relacional
# Base de datos no relacional

# SQLite 


# Tipos de entidades 

# Entidad: Es un objeto o concepto que tiene una existencia independiente

# Atributo: Es una propiedad o característica de una entidad

# Relación: Es una asociación entre dos o más entidades

# ERD - Entity Relationship Diagram

# Un diagrama de entidad-relación (ERD) es una representación gráfica de
# las entidades y sus relaciones en una base de datos. Se utiliza para
# diseñar y visualizar la estructura de una base de datos.

# Un ERD consta de tres componentes principales:

# Entidades: Representadas por rectángulos, son los objetos o conceptos
# que se desean almacenar en la base de datos. Cada entidad tiene un
# nombre y una serie de atributos.
# Atributos: Representados por óvalos, son las propiedades o
# características de una entidad. Cada atributo tiene un nombre y un
# tipo de dato.
# Relaciones: Representadas por rombos, son las asociaciones entre
# entidades. Las relaciones pueden ser de uno a uno, uno a muchos o
# muchos a muchos.

# Tipos de relaciones entre entidades
# Uno a uno (1:1): Cada entidad A se relaciona con una sola entidad B,
# y cada entidad B se relaciona con una sola entidad A. Ejemplo: Un
# empleado tiene un único número de seguro social.

# Uno a muchos (1:N): Cada entidad A se relaciona con varias entidades
# B, pero cada entidad B se relaciona con una sola entidad A. Ejemplo:
# Un autor puede tener varios libros, pero cada libro tiene un solo autor.

# Muchos a uno (N:1): Cada entidad B se relaciona con varias entidades
# A, pero cada entidad A se relaciona con una sola entidad B. Ejemplo:
# Varios libros pueden pertenecer a una sola editorial, pero cada
# editorial puede tener varios libros.

# Muchos a muchos (N:M): Cada entidad A se relaciona con varias
# entidades B, y cada entidad B se relaciona con varias entidades A.
# Ejemplo: Un estudiante puede estar inscrito en varios cursos, y
# cada curso puede tener varios estudiantes.


# Bases de datos relacionales

# Una base de datos relacional es un tipo de base de datos que
# organiza los datos en tablas, donde cada tabla representa una entidad
# y cada fila de la tabla representa una instancia de esa entidad.
# Las columnas de la tabla representan los atributos de la entidad.


# Mapeo de entidades a tablas

# Entidad = Tabla
# Atributo = Columna
# Instancia/Objeto = Fila

# SELECT * FROM estudiantes;

# INSERT INTO estudiantes (nombre, email) 
# VALUES ('Juan', 'juan@test.com');

# INSERT INTO estudiantes (nombre, email)
# VALUES ('Andrea', 'andrea@test.com'), 
# ('Cesar', 'cesar@test.com'), ('Ruben', 'ruben@test.com');

# SELECT nombre, email FROM estudiantes;

# CREATE TABLE carreras (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   nombre TEXT NOT NULL,
#   duracion INTEGER NOT NULL DEFAULT 3
# );

# INSERT INTO carreras (nombre, duracion)
# VALUES ('Ingenieria de Sistemas' , 5), 
# ('Ingenieria de Software', 4), 
# ('Ingenieria de Datos', 6);

# INSERT INTO carreras (nombre)
# VALUES ('Licenciatura en Informatica')

# ALTER TABLE estudiantes
# ADD CONSTRAINT carrera_id FOREIGN KEY("id") REFERENCES "carreras"("id");

# FOREIGN KEY("carrera_id") REFERENCES "carreras"("id")

# UPDATE estudiantes SET carrera_id = 2;

# SELECT * FROM estudiantes
# WHERE carrera_id = 2;

# UPDATE estudiantes SET carrera_id = 1
# WHERE id = 1;

# ALTER TABLE estudiantes
# ADD COLUMN edad INTEGER;

# SELECT * FROM estudiantes
# WHERE edad <= 25;

# Crear una tabla
# Agregar al menos 3 registros, con codigo
# Modificar un registro
# Traer todos los registros
# Hacer un filtro con where

# SELECT * FROM products
# WHERE price > 100 OR categoryID = 1;

# SELECT * FROM products
# WHERE NOT supplierID = 1;

# SELECT * FROM shippers

# SELECT * FROM shippers
# WHERE shipperName IS NULL;

# SELECT AVG(price) FROM products

# SELECT COUNT(*) AS total_empleados FROM employees

# SELECT lastname AS apellido FROM employees;

# SELECT lastname AS apellido FROM employees
# WHERE apellido LIKE '%d%';

# SELECT lastname AS apellido FROM employees
# WHERE apellido LIKE '%o__';


# Peacock
# Dodsworth


# SELECT * FROM estudiantes WHERE ci = 12345678;

