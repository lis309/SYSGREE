# Importar flask y otros metodos
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Importar mi modelo
from models.Modelos import Ingrediente

# Conexion a la bd
from utils.db import db

#Importar el decorador
from .validateRol import usuarioAdminRequired
from .logout import cerrarSesion

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

    nuevoIngrediente = Ingrediente(nombre, descripcion, tipoSabor, categoria)

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


@ingredients.route("/eliminar/<codigoIngrediente>")
@usuarioAdminRequired
@cerrarSesion
def eliminarIngrediente(codigoIngrediente):
    ingredient = Ingrediente.query.get(codigoIngrediente)

    db.session.delete(ingredient)
    db.session.commit()
    
    flash("El ingrediente se eliminó correctamente", "success")

    return redirect(url_for("ingredients.consultarIngrediente"))
