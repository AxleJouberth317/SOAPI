from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt

from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.server.django import DjangoApplication
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc
from spyne.util.django import DjangoComplexModel, DjangoServiceBase
from spyne.service import ServiceBase

from .models import Post


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hola, %s' % name

'''class PostService(ServiceBase):
	@rpc(Unicode, _returns=Unicode)
	def create(ctx, str):
		post = Post(name=str)
		post.save
		print ("EXITO")
		return 'Success'

	@rpc(_returns=Iterable(Unicode))
	def get(ctx):
		return Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')'''

class GetService(ServiceBase):
	@rpc(Unicode, _returns=Unicode)
	def get(ctx, name):
		return Post.objects.filter(name)
		#return Post.objects.filter(name)


app = Application([HelloWorldService, GetService],
    'spyne.examples.django',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

hello_world_service = csrf_exempt(DjangoApplication(app))



