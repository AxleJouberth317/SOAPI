from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView,ListView, View
from django.urls import reverse_lazy 
from apps.movies.forms import RegistroForm 
from .models import Pelicula, Registro, Persona, Planes
from django.shortcuts import render,get_list_or_404, get_object_or_404,redirect 
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse 
from .controller import PeliculasVistas, ListadoPeliculas
from .forms import CalificacionForm,CalificacionForm2


#servicio

from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.server.django import DjangoApplication
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc
from spyne.util.django import DjangoComplexModel, DjangoServiceBase
from spyne.service import ServiceBase

#from .models import Planes

class HelloWorldService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def say_hello(ctx):
        plans = Planes.objects.all()
        personas = Persona.objects.all()
        for plan in plans:
            yield ("Tipo de Plan : "+str(plan.tipoplan)+", Valor: "+str(plan.valor))

def ListarUsuario(request): 
	model=PeliculasVistas()
	context = {'object_list':model}
	return render(request,'listar.html',context)

def ListarPeliculas(request):
	model=ListadoPeliculas()
	context = {'object_list':model}
	return render(request,'listar2.html',context)

def add(request): 

  if request.method == "POST": 
    # add to the DB 
    form = CalificacionForm2(request.POST) 

    if form.is_valid(): 
      cli=form.cleaned_data['cliente']
      peli=form.cleaned_data['pelicula']
      califi=form.cleaned_data['calificacion']
      per=Persona.objects.get(id=cli)
      pel=Pelicula.objects.get(id=peli)
      p= Registro(cliente=per,pelicula=pel,calificacion=califi)
      #print(form.cleaned_data['cliente'])
      p.save()
      #form.save() 

      return HttpResponseRedirect(reverse('peliculas_listar')) 

    print("No es valido.....................")
    return HttpResponseRedirect(reverse('peliculas_listar')) 

  else: 
    # show the form 
    form = CalificacionForm2()
    context={'form':form}
    return render(request, 'add.html', context)

def edit(request, id): 
  post = get_object_or_404(Registro, id=id) 
  if request.method == "POST": 
    # update DB 
    form = CalificacionForm(request.POST, instance=post) 
    if form.is_valid(): 
      post = form.save(commit=False) 
      post.save() 
      return redirect('peliculas_listar') 
  else: 

    # show the form 
    form = CalificacionForm(instance=post)   

  context = { 'form': form }
  return render(request, 'actualizar.html', context) 

def delete(request, id): 

  post = get_object_or_404(Registro, id=id) 

  post.delete() 

  return redirect('peliculas_listar')




app = Application(
    [HelloWorldService],
    tns='django.soap.requisitos',
    #spyne.examples.django,
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

hello_world_service = csrf_exempt(DjangoApplication(app))





