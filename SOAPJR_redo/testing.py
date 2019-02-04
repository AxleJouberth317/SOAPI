from suds.client import Client
from suds.cache import NoCache


#url del servicio :http://127.0.0.1:8000/api/?wsdl

my_client = Client('http://127.0.0.1:8000/api?WSDL',cache=NoCache())


print (my_client)
print(my_client.service.say_hello('Pedro',4))
#my_client.service.create('Jouberth')"
print(my_client.service.get('Jouberth'))

