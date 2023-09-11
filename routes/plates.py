# Importar flask y otros metodos
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Importar mi modelo
from models.Modelos import Plato

# Conexion a la bd
from utils.db import db

#Importar el decorador
from .validateRol import usuarioAdminRequired

plates = Blueprint("plates", __name__)

@plates.route("/")
def home():
    return render_template("index.html")

@plates.route("/listarPlato")
@usuarioAdminRequired
def consultarPlato():
    plates = Plato.query.all()
    return render_template("plato/Consultar_Plato.html", plates=plates)


@plates.route("/registrarPlato")
@usuarioAdminRequired
def capturarPlato():
    return render_template("plato/RegistrarPlato.html")


@plates.route("/registrarPlate", methods=["POST"])
@usuarioAdminRequired
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

    return redirect(url_for("plates.consultarPlato"))


@plates.route("/actualizarPlato/<codigoPlato>", methods=["POST", "GET"])
@usuarioAdminRequired
def actualizarPlato(codigoPlato):

    plate = Plato.query.get(codigoPlato)

    if request.method == "POST":
        plate.nombrePlato = request.form["nombre"]
        plate.descripcionPlato = request.form["descripcion"]
        plate.precioPlato = request.form["precio"]

        db.session.commit()
        
        return redirect(url_for("plates.consultarPlato"))

    return render_template("plato/ActualizarPlato.html", plate=plate)


@plates.route("/eliminarPlato/<codigoPlato>")
@usuarioAdminRequired
def eliminarPlato(codigoPlato):
    plate = Plato.query.get(codigoPlato)

    db.session.delete(plate)
    db.session.commit()

    return redirect(url_for("plates.consultarPlato"))
