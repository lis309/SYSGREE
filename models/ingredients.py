# Traer la dependencia - app o .
from utils.db import db


# Crear modelos
class rolUsuario(db.Model):
    # Definir atributos
    __tablename__ = "rolUsuarios"
    idRolUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreRolUsuario = db.Column(db.String(120))

    def __init__(self, nombreRolUusario):
        self.nombreRolUsuario = nombreRolUusario


class Usuario(db.Model):
    # Definir atributos
    __tablename__ = "usuarios"
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correoUsuario = db.Column(db.String(120))
    passwordUsuario = db.Column(db.String(120))
    # Clave foránea
    idRolUsuarioFK = db.Column(db.Integer, db.ForeignKey("rolUsuarios.idRolUsuario"))

    def __init__(self, correoUsuario, passwordUsuario, idRolUsuarioFK):
        self.correoUsuario = correoUsuario
        self.passwordUsuario = passwordUsuario
        self.idRolUsuarioFK = idRolUsuarioFK


class Ingrediente(db.Model):
    # Definir los atributos
    __tablename__ = "ingredientes"
    codigoIngrediente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreIngrediente = db.Column(db.String(120), nullable=True)
    descripcionIngrediente = db.Column(db.String(120), nullable=True)
    tipoSaborIngrediente = db.Column(db.String(128), nullable=True)
    categoriaIngrediente = db.Column(db.String(120), nullable=True)

    def __init__(self, nombreIngrediente, descripcionIngrediente, tipoSaborIngrediente, categoriaIngrediente):
        self.nombreIngrediente = nombreIngrediente
        self.descripcionIngrediente = descripcionIngrediente
        self.tipoSaborIngrediente = tipoSaborIngrediente
        self.categoriaIngrediente = categoriaIngrediente


class Plato(db.Model):
    # Definir atributos
    __tablename__ = "platos"
    codigoPlato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrePlato = db.Column(db.String(120))
    descripcionPlato = db.Column(db.String(120))
    precioPlato = db.Column(db.String(120))

    def __init__(self, nombrePlato, descripcionPlato, precioPlato):
        self.nombrePlato = nombrePlato
        self.descripcionPlato = descripcionPlato
        self.precioPlato = precioPlato


class IngredientePlato(db.Model):
    # Definir atributos
    __tablename__ = "ingredientesPlato"

    # Claves foráneas
    codigoIngredienteFK = db.Column(
        db.Integer, db.ForeignKey("ingredientes.codigoIngrediente"), primary_key=True
    )
    codigoPlatoFK = db.Column(
        db.Integer, db.ForeignKey("platos.codigoPlato"), primary_key=True
    )

    def __init__(self, codigoIngredienteFK, codigoPlatoFK):
        self.codigoIngredienteFK = codigoIngredienteFK
        self.codigoPlatoFK = codigoPlatoFK
