# Importar flask y otros metodos
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar mi modelo
from models.Modelos import Ingrediente

# Conexion a la bd
from utils.db import db

#Importar el decorador
from .validateRol import usuarioAdminRequired
from .logout import cerrarSesion
from sqlalchemy.exc import IntegrityError

ingredients = Blueprint("ingredients", __name__)

@ingredients.route("/listarIngrediente")
@usuarioAdminRequired
@cerrarSesion
def consultarIngrediente():
    ingredients = Ingrediente.query.all()
    return render_template("ingrediente/Consultar_Ingrediente.html", ingredients=ingredients)


@ingredients.route("/registrarIngrediente")
@usuarioAdminRequired
@cerrarSesion
def capturarIngrediente():
    return render_template("ingrediente/RegistrarIngrediente.html")


@ingredients.route("/registrarIngredient", methods=["POST"])
@usuarioAdminRequired
@cerrarSesion
def registrarIngrediente():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    tipoSabor = request.form["tipoSabor"]
    categoria = request.form["categoria"]

    estado = "Activo" 

    nuevoIngrediente = Ingrediente(nombre, descripcion, tipoSabor, categoria, estado)

    db.session.add(nuevoIngrediente)
    db.session.commit()

    flash("El ingrediente se registró correctamente", "success")

    return redirect(url_for("ingredients.consultarIngrediente"))


@ingredients.route("/actualizarIngrediente/<codigoIngrediente>", methods=["POST", "GET"])
@usuarioAdminRequired
@cerrarSesion
def actualizarIngrediente(codigoIngrediente):

    ingrediente = Ingrediente.query.get(codigoIngrediente)

    if request.method == "POST":
        ingrediente.nombreIngrediente = request.form["nombre"]
        ingrediente.descripcionIngrediente = request.form["descripcion"]
        ingrediente.tipoSaborIngrediente = request.form["tipoSabor"]
        ingrediente.categoriaIngrediente = request.form["categoria"]

        db.session.commit()
        
        flash("El ingrediente se actualizó correctamente", "success")
                
        return redirect(url_for("ingredients.consultarIngrediente"))

    return render_template("ingrediente/ActualizarIngrediente.html", ingrediente=ingrediente)


@ingredients.route("/eliminarIngrediente/<codigoIngrediente>", methods=['POST'])
@usuarioAdminRequired
@cerrarSesion
def eliminarIngrediente(codigoIngrediente):
    try:
        ingredient = Ingrediente.query.get(codigoIngrediente)

        if ingredient:
            # Actualiza el campo 'estado' en lugar de eliminar físicamente
            ingredient.estadoIngrediente = ("Inactivo")
            db.session.commit()
            flash("El ingrediente se eliminó correctamente", "success")
            return jsonify({'message': 'Plato eliminado con éxito'})
        else:
            flash("No se pudo encontrar el ingrediente a eliminar", "error")
            return jsonify({'message': 'Error al eliminar el plato'})
    except IntegrityError as e:
        # Si hay una violación de la clave externa, maneja el error
        db.session.rollback()
        flash(f"No se puede eliminar el plato debido a restricciones de integridad referencial: {str(e)}", "error")
        return jsonify({'message': f'Error al eliminar el plato debido a restricciones de integridad referencial: {str(e)}'})

        