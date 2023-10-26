from flask import jsonify, Blueprint, request
#Importar modelos
from models.Modelos import Ingrediente, IngredientePlato
# Conexion a la bd
from utils.db import db
#Importar el decorador
from .validateRol import usuarioClientRequired
from .logout import cerrarSesion

listaIngredientes = Blueprint("listaIngredientes", __name__)

# Definir una ruta para obtener los nombres de los ingredientes en formato JSON
@listaIngredientes.route('/obtener_ingredientes', methods=['GET'])
@usuarioClientRequired
@cerrarSesion
def obtener_ingredientes():
    # Obtén el ID del plato de la solicitud
    plato_id = request.args.get("id")

    # Realiza una consulta para obtener los ingredientes del plato específico
    ingredientes = db.session.query(Ingrediente.nombreIngrediente).join(
        IngredientePlato, IngredientePlato.codigoIngredienteFK == Ingrediente.codigoIngrediente
    ).filter(IngredientePlato.codigoPlatoFK == plato_id).all()

    # Procesa los resultados y devuelve los nombres de los ingredientes en formato JSON
    ingredientes = [ingrediente for (ingrediente,) in ingredientes]
    
    return jsonify(ingredientes)