from flask import jsonify, Blueprint, request
from sqlalchemy import and_
#Importar modelos
from models.Modelos import Ingrediente, IngredientePlato, Pedido, Plato
# Conexion a la bd
from utils.db import db
#Importar el decorador
from .validateRol import usuarioClientRequired
from .logout import cerrarSesion

listaIngredientes = Blueprint("listaIngredientes", __name__)

@listaIngredientes.route('/obtener_ingredientes', methods=['GET'])
@usuarioClientRequired
@cerrarSesion
def obtener_ingredientes():
    # Obtén el ID del plato de la solicitud
    plato_id = request.args.get("id")

    # Realiza una consulta para obtener los ingredientes del plato específico con estado "Activo"
    ingredientes = db.session.query(Ingrediente.nombreIngrediente).join(
        IngredientePlato, IngredientePlato.codigoIngredienteFK == Ingrediente.codigoIngrediente
    ).filter(
        and_(
            IngredientePlato.codigoPlatoFK == plato_id,
            Ingrediente.estadoIngrediente == "Activo"
        )
    ).all()

    # Procesa los resultados y devuelve los nombres de los ingredientes en formato JSON
    ingredientes = [ingrediente for (ingrediente,) in ingredientes]

    return jsonify(ingredientes)


@listaIngredientes.route('/realizar_pedido', methods=['POST'])
@usuarioClientRequired
@cerrarSesion
def realizar_pedido():
    try:
        data = request.json
        plato_id = data.get("plato_id")
        ingredientes = data.get("ingredientes")
        cantidad = data.get("cantidad")
        metodo_pago = data.get("metodo_pago")

        nombrePlato = db.session.query(Plato.nombrePlato).filter(Plato.codigoPlato == plato_id).first()

        nombre = str(nombrePlato[0])

        precioPlato = db.session.query(Plato.precioPlato).filter(Plato.codigoPlato == plato_id).first()

        valor = (int(precioPlato[0]) * cantidad)

        ingredientes_pedido = {
            f'ingrediente_{i+1}': ingrediente if ingrediente else None for i, ingrediente in enumerate(ingredientes)
        }

        nuevo_pedido = Pedido(
            nombrePlatoPedido = nombre,
            **ingredientes_pedido,
            metodoPago = str(metodo_pago),
            valorPedido = valor,
            cantidadPedido = cantidad,
            estadoPedido = "Espera"
        )

        db.session.add(nuevo_pedido)
        db.session.commit()

        return jsonify({"mensaje": "Pedido realizado con éxito"})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

