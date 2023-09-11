# Importar flask y otros metodos
from flask import Blueprint, render_template

#Importar el decorador
from .validateRol import usuarioClientRequired

menuClient = Blueprint("menu", __name__)

@menuClient.route("/menu")
@usuarioClientRequired
def menuCliente():
    return render_template("Cliente/menuCliente.html")

@menuClient.route("/Entradas")
@usuarioClientRequired
def Entradas():
    return render_template("menus/Entradas.html")

@menuClient.route("/Adicionales")
@usuarioClientRequired
def Adicionales():
    return render_template("menus/Adicionales.html")

@menuClient.route("/bebidas")
@usuarioClientRequired
def bebidas():
    return render_template("menus/bebidas.html")

@menuClient.route("/Infantil")
@usuarioClientRequired
def Infantil():
    return render_template("menus/Infantil.html")

@menuClient.route("/Jugos")
@usuarioClientRequired
def Jugos():
    return render_template("menus/Jugos.html")

@menuClient.route("/robalo")
@usuarioClientRequired
def robalo():
    return render_template("menus/robalo.html")

@menuClient.route("/salmon")
@usuarioClientRequired
def salmon():
    return render_template("menus/salmon.html")

@menuClient.route("/Truchas")
@usuarioClientRequired
def Truchas():
    return render_template("menus/Truchas.html")

@menuClient.route("/Variedades")
@usuarioClientRequired
def Variedades():
    return render_template("menus/Variedades.html")

@menuClient.route("/Variedad")
@usuarioClientRequired
def Variedad():
    return render_template("menus/Variedades2.html")
