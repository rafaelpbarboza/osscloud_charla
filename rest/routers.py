from rest import api_rest
from rest.resources import Rest

api_rest.add_resource(Rest, '/hola/int:id')
