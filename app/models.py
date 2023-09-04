#Traer la dependencia - app o .
from . import db

#Crear modelos
class rolUsuario(db.Model):
    #Definir atributos
    __tablename__ = "rolUsuarios"
    idRolUsuario = db.Column(db.Integer, primary_key = True, autoincrement = True) 
    nombreRolUsuario = db.Column(db.String(120))
    
    
class Usuario(db.Model):
    #Definir atributos
    __tablename__ = "usuarios"
    idUsuario = db.Column(db.Integer, primary_key = True, autoincrement = True)
    correoUsuario = db.Column(db.String(120))
    passwordUsuario = db.Column(db.String(120))
    #Clave foránea
    idRolUsuarioFK = db.Column(db.Integer, db.ForeignKey('rolUsuarios.idRolUsuario'))

class Ingrediente(db.Model):
    #Definir los atributos
    __tablename__ = "ingredientes"
    codigoIngrediente = db.Column(db.Integer, primary_key = True, autoincrement = True) 
    nombreIngrediente = db.Column(db.String(120), nullable = True)
    tipoSaborIngrediente = db.Column(db.String(128), nullable = True)
    categoriaIngrediente = db.Column(db.String(120), nullable = True)
    #relaciones SQL alchemy
    #ventas = db.relationship('Venta', backref = "cliente", lazy = "dynamic")

class Plato(db.Model):
    #Definir atributos
    __tablename__ = "platos"
    codigoPlato = db.Column(db.Integer, primary_key = True, autoincrement = True) 
    nombrePlato = db.Column(db.String(120))
    descripcionPlato = db.Column(db.String(120))
    precioPlato = db.Column(db.String(120))
    
    
class IngredientePlato(db.Model):
    # Definir atributos
    __tablename__ = "ingredientesPlato"
    
    # Claves foráneas
    codigoIngredienteFK = db.Column(db.Integer, db.ForeignKey('ingredientes.codigoIngrediente'), primary_key=True)
    codigoPlatoFK = db.Column(db.Integer, db.ForeignKey('platos.codigoPlato'), primary_key=True)

