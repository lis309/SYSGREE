# Importar flask y otros metodos
from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash, session
#Importar werkzeug para encriptar la contraseña
from werkzeug.security import generate_password_hash, check_password_hash

# Importar mi modelo
from models.Modelos import Usuario

# Conexion a la bd
from utils.db import db

app = Flask(__name__)

app.secret_key = 'h@K45pQwT#m7FgZnD$78vL!xJl5C*+yRb'

Login = Blueprint ("login", __name__)

@Login.route('/')
def home():
    return render_template('index.html')

@Login.route('/registrar')
def registrar():
    return render_template('Login/Registrar.html')

@Login.route('/crearCuenta', methods=['POST'])
def crearCuenta():
    if request.method == 'POST':
        # Obtener los datos del formulario de registro
        email = request.form['correo']
        password = request.form['password']
        confirmarPassword = request.form['confirmarPassword']

        if not email:
            flash('El correo esta vació', 'info')
            return redirect(url_for('login.registrar'))
        else:
            # Verificar si el correo ya está en uso
            correoExistente = Usuario.query.filter_by(correoUsuario=email).first()
            if correoExistente:
                flash('El correo ya está en uso. Por favor, elige otro.', 'info')
                return redirect(url_for('login.registrar'))

        if not password or not confirmarPassword:
            flash('Ningún campo de contraseña debe estar vació', 'warning')
            return redirect(url_for('login.registrar')) 
        else:
            # Validar que la contraseña y la confirmación coincidan
            if password != confirmarPassword:
                flash('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.', 'warning')
                return redirect(url_for('login.registrar'))
            else:
                # Hash de la contraseña antes de guardarla en la base de datos
                hashed_password = generate_password_hash(password, method='sha256')

                # Crear un nuevo usuario y guardar el hash de la contraseña en la base de datos
                nuevo_usuario = Usuario(correoUsuario=email, passwordUsuario=hashed_password, idRolUsuarioFK=2)
                db.session.add(nuevo_usuario)
                db.session.commit()

        # Redirigir al usuario a la página de inicio de sesión u otra página
        flash('¡Registro exitoso! Por favor, inicia sesión.', 'success')
        return redirect(url_for('login.iniciarSesion'))
    
    # Si la solicitud no es POST, simplemente renderiza el formulario de registro
    flash('Los campos estan vacíos', 'info')
    return redirect(url_for('login.registrar'))

@Login.route('/iniciarSesion')
def iniciarSesion():
    return render_template('Login/login.html')


@Login.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('correo')
        password = request.form.get('password')

        if not email:
            flash('Por favor, completa el correo.', 'warning')
            return redirect(url_for('login.iniciarSesion'))
        
        elif not password:
            flash('Por favor, completa la contraseña.', 'warning')
            return redirect(url_for('login.iniciarSesion'))
        
        user = Usuario.query.filter_by(correoUsuario=email).first()

        if user and check_password_hash(user.passwordUsuario, password):
            # Autenticación exitosa, guarda el rol en la sesión
            session['rol'] = user.idRolUsuarioFK
            
            # Redirige según el rol del usuario
            if user.idRolUsuarioFK == 1:  # Rol de administrador 
                return redirect(url_for('menuAdmin.menuAdmin'))  # Ruta para administradores
            elif user.idRolUsuarioFK == 2:  # Rol de cliente 
                return redirect(url_for('menu.menuCliente'))  # Ruta para clientes

        flash('Credenciales incorrectas. Por favor, inténtalo de nuevo.', 'warning')
        return render_template('Login/login.html')

    return render_template('Login/login.html')


