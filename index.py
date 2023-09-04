# Importar app
from app import app

# Importar SQLAlchemy y otros módulos necesarios
from utils.db import db

# Importar modelos SQLAlchemy
from models.ingredients import rolUsuario, Usuario, Ingrediente, Plato, IngredientePlato

# Registrar la aplicación Flask con SQLAlchemy
db.init_app(app)

# Crear todas las tablas de la base de datos
with app.app_context():
    db.create_all()

# Verificar si el script se ejecuta directamente como el archivo principal
if __name__ == "__main__":
    # Iniciar la aplicación Flask en modo de depuración
    app.run(debug=True)

