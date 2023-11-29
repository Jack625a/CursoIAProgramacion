--Base de datos tienda

CREATE DATABASE tienda;

USE tienda;

CREATE TABLE productos(
    id INT AUTO_INCREMENT,
    nombre VARCHAR(50),
    precio DECIMAL(10,2),
    PRIMARY KEY(id)
);

insert into productos(nombre, precio) VALUES('Pantalon', '100');

SELECT * FROM productos;    

CREATE TABLE usuarios(
    id INT AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(50),
    PRIMARY KEY(id)
);

insert into usuarios(nombre, apellido, email, password) VALUES('Juan', 'Perez', 'XXXXXXXXXXXXXX', '123456');