# Importar flask y otros metodos
from flask import Blueprint, render_template

menuClient = Blueprint("menu", __name__)

@menuClient.route("/menu")
def menuCliente():
    return render_template("Cliente/menuCliente.html")

@menuClient.route("/Entradas")
def Entradas():
    return render_template("menus/Entradas.html")

@menuClient.route("/Adicionales")
def Adicionales():
    return render_template("menus/Adicionales.html")

@menuClient.route("/bebidas")
def bebidas():
    return render_template("menus/bebidas.html")

@menuClient.route("/Infantil")
def Infantil():
    return render_template("menus/Infantil.html")

@menuClient.route("/Jugos")
def Jugos():
    return render_template("menus/Jugos.html")

@menuClient.route("/robalo")
def robalo():
    return render_template("menus/robalo.html")

@menuClient.route("/salmon")
def salmon():
    return render_template("menus/salmon.html")

@menuClient.route("/Truchas")
def Truchas():
    return render_template("menus/Truchas.html")

@menuClient.route("/Variedades")
def Variedades():
    return render_template("menus/Variedades.html")

@menuClient.route("/Variedad")
def Variedad():
    return render_template("menus/Variedades2.html")
