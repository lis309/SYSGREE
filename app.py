# Importar flask
from flask import Flask
from flask_session import Session

# Importar blueprint ingredients
from routes.ingredients import ingredients

# Importar blueprint plates
from routes.plates import plates

# Importar blueprint login
from routes.login import Login

# Importar blueprint menuCliente
from routes.menuCliente import menuClient

# Importar blueprint menuAdministrador
from routes.menuAdministrador import menuAdministrador

#Importar blueprint de cerrar sesion
from routes.logout import logout

#Importar blueprint de listaIngredientes
from routes.listaIngredientes import listaIngredientes

#Importar blueprint de listaIngredientes
from routes.comandas import orders

# Importar la clase SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Definir objeto flask
app = Flask(__name__)

# Configurar la URL de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/sysgree'

# Desactivar el seguimiento de notificaciones de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'h@K45pQwT#m7FgZnD$78vL!xJl5C*+yRb'

# Configura la extensión Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'  # Puedes elegir un método de almacenamiento diferente si lo deseas
Session(app)

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

# Traer la función del blueprint
app.register_blueprint(ingredients)

# Traer la función del blueprint
app.register_blueprint(plates)

# Traer la función del blueprint
app.register_blueprint(Login)

# Traer la función del blueprint
app.register_blueprint(menuClient)

# Traer la función del blueprint
app.register_blueprint(menuAdministrador)

# Traer la función del blueprint
app.register_blueprint(logout)

# Traer la función del blueprint
app.register_blueprint(listaIngredientes)

# Traer la función del blueprint
app.register_blueprint(orders)

