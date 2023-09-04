#Traer la dependencia blueprint
from flask import Blueprint

#Definir objeto blueprint
mi_blueprint = Blueprint('mi_blueprint', __name__, url_prefix = '/ejemplo')

#Definir ruta
@mi_blueprint.route('/prueba')
def index():
    return "Hola, me llamo merlina"