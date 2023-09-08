# Importar flask y otros metodos
from flask import Blueprint, render_template, request, redirect, url_for
#Importar werkzeug para encriptar la contraseña
from werkzeug.security import generate_password_hash, check_password_hash

# Importar mi modelo
from models.Modelos import Usuario

# Conexion a la bd
from utils.db import db

Login = Blueprint("login", __name__)

@Login.route('/registrar')
def registrar():
    return render_template('Login/Registrar.html')

@Login.route('/crearCuenta')
def crearCuenta():
    return render_template('Login/Registrar.html')

@Login.route('/iniciarSesion')
def iniciarSesion():
    return render_template('Login/login.html')

@Login.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario de inicio de sesión
        correo = request.form['correo']
        password = request.form['password']

        # Realizar la lógica de autenticación aquí (por ejemplo, consultar la base de datos)
        user = Usuario.query.filter_by(correoUsuario=correo, passwordUsuario=password).first()

        if user:
            # Autenticación exitosa, redirigir a una página de inicio o dashboard
            return render_template('plato/Consultar_Plato.html')
        
        else:
             return render_template('Login/login.html', error = 'Credenciales incorrectas')

    return redirect(url_for('login.iniciarSesion'))


