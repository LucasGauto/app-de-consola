CREATE DATABASE app_consola;
USE app_consola;

CREATE TABLE users(
    id INTEGER(25) PRIMARY KEY IDENTITY NOT NULL,
    nombre VARCHAR(50),
    apellidos VARCHAR(50),
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT uq_email UNIQUE (email)
)

CREATE TABLE notes(
    id INTEGER(25) PRIMARY KEY IDENTITY NOT NULL,
    usuario_id INT(25) NOT NULL,
    titulo VARCHAR(255) not null,
    descripcion MEDIUMTEXT,
    fecha DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES users(id)
)