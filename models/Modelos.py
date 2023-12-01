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
    estadoIngrediente = db.Column(db.String(50))

    def __init__(self, nombreIngrediente, descripcionIngrediente, tipoSaborIngrediente, categoriaIngrediente, estadoIngrediente):
        self.nombreIngrediente = nombreIngrediente
        self.descripcionIngrediente = descripcionIngrediente
        self.tipoSaborIngrediente = tipoSaborIngrediente
        self.categoriaIngrediente = categoriaIngrediente
        self.estadoIngrediente = estadoIngrediente


class Plato(db.Model):
    # Definir atributos
    __tablename__ = "platos"
    codigoPlato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrePlato = db.Column(db.String(120))
    descripcionPlato = db.Column(db.String(120))
    precioPlato = db.Column(db.String(120))
    estadoPlato = db.Column(db.String(50))

    def __init__(self, nombrePlato, descripcionPlato, precioPlato, estadoPlato):
        self.nombrePlato = nombrePlato
        self.descripcionPlato = descripcionPlato
        self.precioPlato = precioPlato
        self.estadoPlato = estadoPlato


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


class Pedido(db.Model):
    # Definir los atributos
    __tablename__ = "pedidos"
    codigoPedido = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrePlatoPedido = db.Column(db.String(120), nullable=True)
    ingrediente_1 = db.Column(db.String(120), nullable=True)
    ingrediente_2 = db.Column(db.String(120), nullable=True)
    ingrediente_3 = db.Column(db.String(120), nullable=True)
    ingrediente_4 = db.Column(db.String(120), nullable=True)
    ingrediente_5 = db.Column(db.String(120), nullable=True)
    ingrediente_6 = db.Column(db.String(120), nullable=True)
    ingrediente_7 = db.Column(db.String(120), nullable=True)
    ingrediente_8 = db.Column(db.String(120), nullable=True)
    ingrediente_9 = db.Column(db.String(120), nullable=True)
    ingrediente_10 = db.Column(db.String(120), nullable=True)
    ingrediente_11 = db.Column(db.String(120), nullable=True)
    ingrediente_12 = db.Column(db.String(120), nullable=True)
    ingrediente_13 = db.Column(db.String(120), nullable=True)
    ingrediente_14 = db.Column(db.String(120), nullable=True)
    ingrediente_15 = db.Column(db.String(120), nullable=True)
    ingrediente_16 = db.Column(db.String(120), nullable=True)
    ingrediente_17 = db.Column(db.String(120), nullable=True)
    ingrediente_18 = db.Column(db.String(120), nullable=True)
    ingrediente_19 = db.Column(db.String(120), nullable=True)
    ingrediente_20 = db.Column(db.String(120), nullable=True)
    metodoPago = db.Column(db.String(120), nullable=True)
    valorPedido = db.Column(db.Integer, nullable=True)
    estadoPedido = db.Column(db.String(50))

    def __init__(self, 
                nombrePlatoPedido, 
                ingrediente_1, 
                ingrediente_2, 
                ingrediente_3, 
                ingrediente_4, 
                ingrediente_5, 
                ingrediente_6, 
                ingrediente_7, 
                ingrediente_8, 
                ingrediente_9,
                ingrediente_10,
                ingrediente_11,
                ingrediente_12,
                ingrediente_13,
                ingrediente_14,
                ingrediente_15,
                ingrediente_16,
                ingrediente_17,
                ingrediente_18,
                ingrediente_19,
                ingrediente_20,
                metodoPago,
                valorPedido,
                estadoPedido):
        self.nombrePlatoPedido = nombrePlatoPedido
        self.ingrediente_1 = ingrediente_1
        self.ingrediente_2 = ingrediente_2
        self.ingrediente_3 = ingrediente_3
        self.ingrediente_4 = ingrediente_4
        self.ingrediente_5 = ingrediente_5
        self.ingrediente_6 = ingrediente_6
        self.ingrediente_7 = ingrediente_7
        self.ingrediente_8 = ingrediente_8
        self.ingrediente_9 = ingrediente_9
        self.ingrediente_10 = ingrediente_10
        self.ingrediente_11 = ingrediente_11
        self.ingrediente_12 = ingrediente_12
        self.ingrediente_13 = ingrediente_13
        self.ingrediente_14 = ingrediente_14
        self.ingrediente_15 = ingrediente_15
        self.ingrediente_16 = ingrediente_16
        self.ingrediente_17 = ingrediente_17
        self.ingrediente_18 = ingrediente_18
        self.ingrediente_19 = ingrediente_19
        self.ingrediente_20 = ingrediente_20
        self.metodoPago = metodoPago
        self.valorPedido = valorPedido
        self.estadoPedido = estadoPedido