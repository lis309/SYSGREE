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
            if usuario == idRolUsuario:
                return True
            else:
                return "Usuario no encontrado", 404
        else:
            # Manejar el caso en el que el usuario no tiene el rol requerido
            return "Acceso no autorizado", 403  # Devuelve un código de estado 403 (Prohibido), por ejemplo
    else:
        # Manejar el caso en el que el rol de usuario no está en la sesión
        return "Usuario no autenticado", 401  # Devuelve un código de estado 401 (No autorizado), por ejemplo

#Decoradores Personalizados

#Administrador
def usuarioAdminRequired(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if verificarUsuario(1):  # 1 es el rol del administrador
            return func(*args, **kwargs)
        else:
            abort(403)  # Acceso prohibido para otros roles
    return wrapper

#Cliente
def usuarioClientRequired(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if verificarUsuario(2):  # 2 es el rol del cliente
            return func(*args, **kwargs)
        else:
            abort(403)  # Acceso prohibido para otros roles
    return wrapper
    