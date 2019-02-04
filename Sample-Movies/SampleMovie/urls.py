"""SampleMovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include 
from django.contrib.auth.views import LoginView




from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView

from apps.movies.views import hello_world_service, app, HelloWorldService


urlpatterns = [
    url(r'^hello_world/', hello_world_service),
    url(r'^say_hello/', DjangoView.as_view(
        services=[HelloWorldService], tns='spyne.examples.django',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
    url(r'^say_hello_not_cached/', DjangoView.as_view(
        services=[HelloWorldService], tns='spyne.examples.django',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11(),
        cache_wsdl=False)),
    url(r'^api/', DjangoView.as_view(application=app)),

    path('admin/', admin.site.urls),
        url('movies/',include('apps.movies.urls')), 
url('',LoginView.as_view(template_name='login.html'),name='login_usuario'),
]

