from flask import jsonify, Blueprint, request, json
from models.Modelos import Ingrediente, IngredientePlato, Pedido, Plato  # Agrega esta línea
from utils.db import db
from .validateRol import usuarioClientRequired
from .logout import cerrarSesion

listaIngredientes = Blueprint("listaIngredientes", __name__)

@listaIngredientes.route('/obtener_ingredientes', methods=['GET'])
@usuarioClientRequired
@cerrarSesion
def obtener_ingredientes():
    plato_id = request.args.get("id")

    # Modifica la consulta para incluir el nombre del plato
    resultados = db.session.query(Ingrediente.nombreIngrediente, Plato.nombrePlato).join(
        IngredientePlato, IngredientePlato.codigoIngredienteFK == Ingrediente.codigoIngrediente
    ).join(Plato, Plato.id == IngredientePlato.codigoPlatoFK).filter(IngredientePlato.codigoPlatoFK == plato_id).all()

    # Procesa los resultados y devuelve el nombre del plato junto con los ingredientes
    data = {
        "nombre_plato": resultados[0].nombrePlato if resultados else None,
        "ingredientes": [nombre_ingrediente for nombre_ingrediente, _ in resultados]
    }
    
    return jsonify(data)

@listaIngredientes.route('/insertar_pedido', methods=['POST'])
@usuarioClientRequired
@cerrarSesion
def insertar_pedido():
    plato_id = request.json.get("id")
    nombre_plato = request.json.get("nombre_plato")
    ingredientes = request.json.get("ingredientes")
    cantidad = request.json.get("cantidad")
    metodo_pago = request.json.get("metodo_pago")

    ingredientes_json = json.dumps(ingredientes)

    pedido = Pedido(plato_id=plato_id, ingredientes=ingredientes_json, cantidad=cantidad, metodo_pago=metodo_pago, nombre_plato=nombre_plato)
    db.session.add(pedido)
    db.session.commit()

    return jsonify({"message": "Pedido insertado correctamente"})
