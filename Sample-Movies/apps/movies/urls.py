from django.conf.urls import url
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView

from apps.movies.views import hello_world_service, app, HelloWorldService ,ListarUsuario,ListarPeliculas, edit,delete,add
urlpatterns = [
    #url(r'^listar', ListarUsuario, name="usuario_listar"),
    url(r'^listar2', ListarPeliculas, name="peliculas_listar"),
    url(r'^(?P<id>\d+)/actualizar$', edit, name='actualizar-model'),
    url(r'^(?P<id>\d+)/delete$', delete, name='borrar-model'), 
    url(r'^agregar', add, name='agregar-model'),
    url(r'^hello_world/', hello_world_service),
    url(r'^say_hello/', DjangoView.as_view(
        services=[HelloWorldService], tns='spyne.examples.django',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
    url(r'^say_hello_not_cached/', DjangoView.as_view(
        services=[HelloWorldService], tns='spyne.examples.django',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11(),
        cache_wsdl=False)),
    url(r'^api/', DjangoView.as_view(application=app)),
]
"""

urlpatterns = [
	#url(r'^listar', ListarUsuario, name="usuario_listar"),
	url(r'^listar2', ListarPeliculas, name="peliculas_listar"),
	url(r'^(?P<id>\d+)/actualizar$', edit, name='actualizar-model'),
	url(r'^(?P<id>\d+)/delete$', delete, name='borrar-model'), 
	url(r'^agregar', add, name='agregar-model'), 

] """
