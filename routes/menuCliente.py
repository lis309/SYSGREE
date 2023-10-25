# Importar flask y otros metodos
from flask import Blueprint, render_template

#Importar el decorador
from .validateRol import usuarioClientRequired
from .logout import cerrarSesion

menuClient = Blueprint("menu", __name__)

@menuClient.route("/menu")
@usuarioClientRequired
@cerrarSesion
def menuCliente():
    return render_template("Cliente/menuCliente.html")

@menuClient.route("/Entradas")
@usuarioClientRequired
@cerrarSesion
def Entradas():
    return render_template("menus/Entradas.html")

@menuClient.route("/Adicionales")
@usuarioClientRequired
@cerrarSesion
def Adicionales():
    return render_template("menus/Adicionales.html")

@menuClient.route("/bebidas")
@usuarioClientRequired
@cerrarSesion
def bebidas():
    return render_template("menus/bebidas.html")

@menuClient.route("/Infantil")
@usuarioClientRequired
@cerrarSesion
def Infantil():
    return render_template("menus/Infantil.html")

@menuClient.route("/Jugos")
@usuarioClientRequired
@cerrarSesion
def Jugos():
    return render_template("menus/Jugos.html")

@menuClient.route("/robalo")
@usuarioClientRequired
@cerrarSesion
def robalo():
    return render_template("menus/robalo.html")

@menuClient.route("/salmon")
@usuarioClientRequired
@cerrarSesion
def salmon():
    return render_template("menus/salmon.html")

@menuClient.route("/Truchas")
@usuarioClientRequired
@cerrarSesion
def Truchas():
    return render_template("menus/Truchas.html")

@menuClient.route("/Variedades")
@usuarioClientRequired
@cerrarSesion
def Variedades():
    return render_template("menus/Variedades.html")

@menuClient.route("/Variedad")
@usuarioClientRequired
@cerrarSesion
def Variedad():
    return render_template("menus/Variedades2.html")
