# Importar flask
from flask import Flask

# Importar blueprint ingredients
from routes.ingredients import ingredients

# Importar la clase SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Definir objeto flask
app = Flask(__name__)

# Configurar la URL de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/sysgree'

# Desactivar el seguimiento de notificaciones de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mi_clave_secreta_super_segura'

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()


# Traer la función del blueprint
app.register_blueprint(ingredients)


