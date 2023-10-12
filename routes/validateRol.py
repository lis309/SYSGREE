from flask import session
from models.Modelos import Usuario
from functools import wraps
from flask import abort

def verificarUsuario(rolRequerido):
    rolUsuario = session.get('rol')
    if rolUsuario is not None:
        if rolUsuario == rolRequerido:
            # Si el usuario tiene el rol requerido, puedes acceder a sus atributos en tu vista
            idRolUsuario = session.get('idUsuarioRolFK')
            usuario = Usuario.query.get(idRolUsuario)  # Consulta la base de datos para obtener al usuario
            if usuario is not None:
                return True  # Usuario con el rol requerido encontrado
            else:
                return "Usuario no encontrado", 404  # Devuelve un mensaje de error 404
        else:
            # Manejar el caso en el que el usuario no tiene el rol requerido
            return "Acceso no autorizado", 403  # Devuelve un mensaje de error 403 (Prohibido)
    else:
        # Manejar el caso en el que el rol de usuario no está en la sesión
        return "Usuario no autenticado", 401  # Devuelve un mensaje de error 401 (No autorizado)


#Decoradores Personalizados

#Administrador
def usuarioAdminRequired(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'rol' in session and session['rol'] == 1:  # 1 es el rol del administrador
            return func(*args, **kwargs)
        else:
            abort(403)  # Acceso prohibido para otros roles
    return wrapper

#Cliente
def usuarioClientRequired(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'rol' in session and session['rol'] == 2:  # 2 es el rol del cliente
            return func(*args, **kwargs)
        else:
            abort(403)  # Acceso prohibido para otros roles
    return wrapper
    