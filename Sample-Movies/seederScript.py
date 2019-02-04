from django_seed import Seed
import random

import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SampleMovie.settings")
django.setup()

seeder = Seed.seeder()

from apps.movies.models import Planes, Persona, Pelicula, Registro

seeder.add_entity(Planes, 3)
seeder.add_entity(Persona, 50)
seeder.add_entity(Pelicula, 50)
seeder.add_entity(Registro, 50)

inserted_pks = seeder.execute()

seeder.add_entity(Planes, 3, {
    'tipoplan': lambda x: seeder.faker.word(),
    'valor': lambda x: random.randint(10,30),
})

seeder.add_entity(Persona, 50, {
    'nombre': lambda x: seeder.faker.name(),
    'apellido': lambda x: seeder.faker.name(),
    'fecha_nacimiento': lambda x: seeder.faker.date(),
    'ciudad': lambda x: seeder.faker.name(),
    'paisnac': lambda x: seeder.faker.name(),
})

seeder.add_entity(Pelicula, 50, {
    'titulo': lambda x: seeder.faker.word(),
	'director': lambda x: seeder.faker.name(),
    'reparto' : lambda x: seeder.faker.word(),
    
})

seeder.add_entity(Registro, 50, {
	'fecha': lambda x: seeder.faker.date(),
	'hora': lambda x: seeder.faker.time(),
    'calificacion': lambda x: random.randint(1,5),
	})

seeder.execute()
