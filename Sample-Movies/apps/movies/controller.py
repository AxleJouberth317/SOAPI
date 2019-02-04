from .models import Pelicula,Registro, Persona

def PeliculasVistas():
	model=Pelicula.objects.raw('SELECT * FROM pelisvistas2()')
	return model

def ListadoPeliculas():
	model=Registro.objects.raw('SELECT * FROM listadopeliculas()')
	return model