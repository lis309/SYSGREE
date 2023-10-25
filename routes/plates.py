# Importar flask y otros metodos
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Importar mi modelo
from models.Modelos import Plato

# Conexion a la bd
from utils.db import db

#Importar el decorador
from .validateRol import usuarioAdminRequired
from .logout import cerrarSesion

plates = Blueprint("plates", __name__)

@plates.route("/listarPlato")
@usuarioAdminRequired
@cerrarSesion
def consultarPlato():
    plates = Plato.query.all()
    return render_template("plato/Consultar_Plato.html", plates=plates)


@plates.route("/registrarPlato")
@usuarioAdminRequired
@cerrarSesion
def capturarPlato():
    return render_template("plato/RegistrarPlato.html")


@plates.route("/registrarPlate", methods=["POST"])
@usuarioAdminRequired
@cerrarSesion
def registrarPlato():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]

    nombre = request.form.get("nombre")
    descripcion = request.form.get("descripcion")
    precio = request.form.get("precio")

    nuevoPlato = Plato(nombre, descripcion, precio)

    db.session.add(nuevoPlato)
    db.session.commit()
    
    flash("El ingrediente se registró correctamente", "success")

    return redirect(url_for("plates.consultarPlato"))


@plates.route("/actualizarPlato/<codigoPlato>", methods=["POST", "GET"])
@usuarioAdminRequired
@cerrarSesion
def actualizarPlato(codigoPlato):

    plate = Plato.query.get(codigoPlato)

    if request.method == "POST":
        plate.nombrePlato = request.form["nombre"]
        plate.descripcionPlato = request.form["descripcion"]
        plate.precioPlato = request.form["precio"]

        db.session.commit()
        
        flash("El ingrediente se actualizó correctamente", "success")
        
        return redirect(url_for("plates.consultarPlato"))

    return render_template("plato/ActualizarPlato.html", plate=plate)


@plates.route("/eliminarPlato/<codigoPlato>")
@usuarioAdminRequired
@cerrarSesion
def eliminarPlato(codigoPlato):
    plate = Plato.query.get(codigoPlato)

    db.session.delete(plate)
    db.session.commit()

    flash("El ingrediente se eliminó correctamente", "success")

    return redirect(url_for("plates.consultarPlato"))
