# Importar flask y otros metodos
from flask import Blueprint, render_template

#Importar el decorador
from .validateRol import usuarioAdminRequired
from .logout import cerrarSesion

menuAdministrador = Blueprint("menuAdmin", __name__)

@menuAdministrador.route("/menuAdmin")
@usuarioAdminRequired
@cerrarSesion
def menuAdmin():
    return render_template("Administrador/menuAdministrador.html")