CREATE DATABASE agenda;

USE agenda;

DROP TABLE IF EXISTS contactos;

CREATE TABLE contactos (
  id_contacto int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  telefono varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  email varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (idContacto)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

INSERT INTO `contactos` VALUES (1,'Renata','7757512345','renata@correo.com');
INSERT INTO `contactos` VALUES (2,'Salvador','7757523456','salvador@correo.com');
