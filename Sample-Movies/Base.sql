CREATE TABLE movies_planes(
	id serial NOT NULL PRIMARY KEY,
	tipoplan varchar(30),
	valor int
);

CREATE TABLE movies_persona(
	id serial NOT NULL PRIMARY KEY,
	nombre varchar(30),
	apellido varchar(30),
	fecha_nacimiento date,
	ciudad varchar(60),
	paisnac varchar(30),
	tipoplan_id int NOT NULL,
	FOREIGN KEY(tipoplan_id) REFERENCES movies_planes(id)
);

CREATE TABLE movies_pelicula(
	id serial NOT NULL PRIMARY KEY,
	titulo varchar(50),
	director varchar(50),
	reparto varchar(300),
	tipoplan_id int NOT NULL,
	FOREIGN KEY(tipoplan_id) REFERENCES movies_planes(id)
);

CREATE TABLE movies_registro(
	id serial NOT NULL PRIMARY KEY,
	cliente_id int,
	pelicula_id int,
	fecha date,
	hora time,
	calificacion int,
	FOREIGN KEY(cliente_id) REFERENCES movies_persona(id),
	FOREIGN KEY(pelicula_id) REFERENCES movies_pelicula(id)
);

SELECT * FROM movies_registro
SELECT * FROM movies_persona
SELECT * FROM movies_pelicula


create function listadopeliculas()
returns table(id int,titulo varchar,usuario varchar,calificacion int)
as $$
	SELECT movies_registro.id,movies_pelicula.titulo,movies_persona.nombre,calificacion FROM movies_registro,movies_persona,movies_pelicula WHERE movies_persona.id=movies_registro.cliente_id AND movies_pelicula.id=movies_registro.pelicula_id ORDER BY movies_registro.id
$$ language sql;

DROP FUNCTION listadopeliculas()
SELECT * FROM listadopeliculas()
SELECT titulo, usuario from listadopeliculas()
SELECT * FROM listadopeliculas()

