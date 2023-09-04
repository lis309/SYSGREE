from flask import Flask, render_template
from . import ingredientes_blueprint

app = Flask(__name__)

@ingredientes_blueprint.route('/registrar')

def crear_ingrediente():
    return render_template('Registrar_Ingrediente.html')