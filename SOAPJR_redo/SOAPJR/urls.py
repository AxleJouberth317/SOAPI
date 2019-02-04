"""SOAPJR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView

from CRUD.views import hello_world_service, app, HelloWorldService, GetService


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
    url(r'^get_names/', DjangoView.as_view(
        services=[GetService], tns='spyne.examples.django',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
]
