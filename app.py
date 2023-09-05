# Importar flask
from flask import Flask

# Importar blueprint ingredients
from routes.ingredients import ingredients

# Importar blueprint ingredients
from routes.plates import plates

# Importar la clase SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Definir objeto flask
app = Flask(__name__)

# Configurar la URL de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/sysgree'

# Desactivar el seguimiento de notificaciones de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'h@K45pQwT#m7FgZnD$78vL!xJl5C*+yRb'

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()


# Traer la función del blueprint
app.register_blueprint(ingredients)

# Traer la función del blueprint
app.register_blueprint(plates)


