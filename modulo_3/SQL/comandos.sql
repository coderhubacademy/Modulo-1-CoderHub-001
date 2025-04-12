-- Comandos de SQL 

-- Crear base de datos
CREATE DATABASE mi_base_de_datos;

-- Crear tabla
CREATE TABLE usuarios (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  email TEXT
);

-- Insertar datos
INSERT INTO usuarios (nombre, email)
VALUES ('Juan', 'juan@mail.com');

-- Consultar datos
SELECT * FROM usuarios;

-- Consultar columnas específicas

SELECT nombre, email FROM usuarios;

-- Filtrar con WHERE

SELECT * FROM usuarios WHERE nombre = 'Juan';

-- Actualizar datos

UPDATE usuarios SET "nombre" = 'Pedro' WHERE id = 1;

-- Eliminar datos

DELETE FROM usuarios WHERE id = 1;

-- Filtros con operadores

SELECT * FROM productos
WHERE precio > 100;

SELECT * FROM productos
WHERE precio BETWEEN 50 AND 200;

SELECT * FROM productos
WHERE nombre LIKE 'A%';

SELECT * FROM usuarios
WHERE email IS NOT NULL;

SELECT * FROM usuarios
WHERE id NOT IN (1, 2, 3);

-- Ordenar resultados

SELECT * FROM usuarios
ORDER BY nombre ASC;

SELECT * FROM usuarios
ORDER BY nombre DESC;

-- Limitar resultados

SELECT * FROM usuarios
LIMIT 5;

-- Agrupar resultados

SELECT COUNT(*) FROM usuarios;
SELECT COUNT(*) FROM usuarios GROUP BY nombre;
SELECT COUNT(*) FROM usuarios GROUP BY nombre HAVING COUNT(*) > 1;
SELECT AVG(precio) FROM productos;
SELECT SUM(precio) FROM productos;
SELECT MIN(precio) FROM productos;
SELECT MAX(precio) FROM productos;

-- Alterar estructura de una tabla

ALTER TABLE usuarios ADD COLUMN edad INTEGER;
ALTER TABLE usuarios RENAME COLUMN nombre TO nombre_completo;
ALTER TABLE usuarios RENAME TO clientes;
ALTER TABLE clientes DROP COLUMN edad;

--  Relaciones (JOIN)