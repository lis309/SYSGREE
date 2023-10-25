# Importar flask y otros metodos
from flask import Blueprint, render_template, session, redirect, url_for, make_response
from functools import wraps

logout = Blueprint("logout", __name__)

@logout.route('/salir')
def verificar():
    # Elimina la información de inicio de sesión de la sesión
    if 'rol' in session:
        del session['rol']
    if 'idUsuarioRolFK' in session:
        del session['idUsuarioRolFK']
    session['cerrado'] = True  # Marca al usuario como "cerrado"
    
    # Redirige al usuario a la página de inicio
    response = make_response(redirect(url_for('login.home')))
    
    # Configura las directivas de control de caché
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response

#Cerrar sesion
def cerrarSesion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'rol' not in session:
            return redirect(url_for('login.iniciarSesion'))
        return func(*args, **kwargs)  # Llama a la función original
    return wrapper