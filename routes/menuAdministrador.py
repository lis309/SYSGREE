# Importar flask y otros metodos
from flask import Blueprint, render_template

#Importar el decorador
from .validateRol import usuarioAdminRequired

menuAdministrador = Blueprint("menuAdmin", __name__)

@menuAdministrador.route("/menuAdmin")
@usuarioAdminRequired
def menuAdmin():
    return render_template("Administrador/menuAdministrador.html")