CREATE DATABASE 'agenda';

USE 'agenda';

CREATE TABLE contactos(
    id int auto_increment primary key,
    nombre varchar(20),
    telefono varchar(10),
    created timestamp default "now()",
    done boolean default 'f'
);

INSERT INTO 'contactos' (nombre,telefono) VALUES ('Dejha Thoris','123456');
INSERT INTO 'contactos' (nombre,telefono) VALUES ('Jhon Carter','7879456');