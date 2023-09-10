# Importar flask y otros metodos
from flask import Blueprint, render_template

menu = Blueprint("menut", __name__)

@menu.route("/menu")
def menu():
    return render_template("menus/menu.html")

@menu.route("/Entradas")
def Entradas():
    return render_template("menus/Entradas.html")

@menu.route("/Adicionales")
def Adicionales():
    return render_template("menus/Adicionales.html")

@menu.route("/bebidas")
def bebidas():
    return render_template("menus/bebidas.html")

@menu.route("/Infantil")
def Infantil():
    return render_template("menus/Infantil.html")

@menu.route("/Jugos")
def Jugos():
    return render_template("menus/Jugos.html")

@menu.route("/robalo")
def robalo():
    return render_template("menus/robalo.html")

@menu.route("/salmon")
def salmon():
    return render_template("menus/salmon.html")

@menu.route("/Truchas")
def Truchas():
    return render_template("menus/Truchas.html")

@menu.route("/Variedade")
def Variedade():
    return render_template("menus/Variedades.html")

@menu.route("/Variedades2")
def Variedades2():
    return render_template("menus/Variedades2.html")
