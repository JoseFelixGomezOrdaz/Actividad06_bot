CREATE DATABASE bot;

USE bot;

CREATE TABLE comandos_mysql(
    id_comando int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    comando varchar(30) NOT NULL,
    funcion varchar(100) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO comandos_mysql (comando, funcion)
VALUES ('CREATE DATABASE','Se utiliza para crear una nueva base de datos'),
('DROP DATABESE','Se utiliza para eliminar completamente una base de datos existente'),
('CREATE TABLE','Se utiliza para crear una nueva tabla, donde la infomacion almacenada realmente'),
('AFTER TABLE','Se utiliza para modificar una tabla ya existente'),
('DROP TABLE','Se utiliza para eliminar por completo una tabla existente'),
('SELECT','Se utiliza cuando quieres leer (o seleccionar) los registros'),
('INSERT','Se utiliza cuando quieres anadir (o inserter ) nuevos registros'),
('UPDATE','Se utiliza cuando quieres cambiar (o borrar) datos existentes'),
('DELETE','Se utiliza cuando quieres eliminar (o borrar) datos existentes'),
('REPLACE','Se utiliza cuando quieres anadir o cambiar (o reemplazar) datos noevos ya existentes'),
('TRUNCATE','Se utiliza para quieres vaciar (o borrar) todos los datos de la plantilla');







SHOW TABLES;

SELECT * FROM comandos_mysql;

DESCRIBE comandos_mysql;

CREATE USER 'bot'@'localhost' IDENTIFIED BY 'bot.2019';
GRANT ALL PRIVILEGES ON bot.* TO 'bot'@'localhost';
FLUSH PRIVILEGES;
