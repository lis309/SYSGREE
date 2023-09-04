#dependencia para hacer un blueprint 
from flask import Blueprint  

#definimos paquete 'products'
ingredientes_blueprint = Blueprint('ingredientes_blueprint', __name__, url_prefix = '/ingredients', template_folder = 'templates')

from . import routes

