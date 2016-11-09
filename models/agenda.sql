CREATE DATABASE agenda;

USE agenda;

DROP TABLE IF EXISTS contactos;

CREATE TABLE contactos (
  id_contacto int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  telefono varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  email varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (id_contacto)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

INSERT INTO contactos (nombre, telefono, email) VALUES ('Dejah Thoris', '7757512345', 'dejah@barson.com');
INSERT INTO contactos (nombre, telefono, email) VALUES ('Jhon Carter', '7757523456', 'jhon@tierra.com');
INSERT INTO contactos (nombre, telefono, email) VALUES ('Carthoris', '757578788', 'carthoris@correobarson.com');
