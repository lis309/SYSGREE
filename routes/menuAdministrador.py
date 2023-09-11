# Importar flask y otros metodos
from flask import Blueprint, render_template

menuAdministrador = Blueprint("menuAdmin", __name__)

@menuAdministrador.route("/menuAdmin")
def menuAdmin():
    return render_template("Administrador/menuAdministrador.html")