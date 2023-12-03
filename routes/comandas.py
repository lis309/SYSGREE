# Importar flask y otros metodos
from flask import Blueprint, render_template, flash, jsonify

# Importar mi modelo
from models.Modelos import Pedido

# Conexion a la bd
from utils.db import db

from sqlalchemy.exc import IntegrityError

#Importar el decorador
from .validateRol import usuarioAdminRequired
from .logout import cerrarSesion

orders = Blueprint("orders", __name__)

@orders.route("/listarComandas")
@usuarioAdminRequired
@cerrarSesion
def Comandas():
    orders = Pedido.query.all()
    print(orders)
    return render_template("comandas/Comandas.html", orders=orders)


@orders.route("/actualizarEstadoPedido/<codigoPedido>", methods=['POST'])
@usuarioAdminRequired
@cerrarSesion
def entregarPedido(codigoPedido):
    try:
        order = Pedido.query.get(codigoPedido)

        if order:
            # Actualiza el campo 'estado' en lugar de eliminar físicamente
            order.estadoPedido = ("Entregado")
            db.session.commit()
            flash("El pedido fue entregado correctamente", "success")
            return jsonify({'message': 'Pedido entregado con éxito'})
        else:
            flash("No se pudo encontrar el pedido a entregar", "error")
            return jsonify({'message': 'Error al entregar el pedido'})
    except IntegrityError as e:
        # Si hay una violación de la clave externa, maneja el error
        db.session.rollback()
        flash(f"No se puede entregar el pedido debido a restricciones de integridad referencial: {str(e)}", "error")
        return jsonify({'message': f'Error al entregar el pedido debido a restricciones de integridad referencial: {str(e)}'})
