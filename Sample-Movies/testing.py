from suds.client import Client
from suds.cache import NoCache


#url del servicio :http://127.0.0.1:8000/api/?wsdl
wsdl = 'http://127.0.0.1:8000/api?WSDL'
my_client = Client(wsdl)

#my_client = Client('http://127.0.0.1:8000/api?WSDL',cache=NoCache())


print (my_client)
print(my_client.service.say_hello())



#python lib/python2.7/site-packages/pgadmin4/pgAdmin4.py

