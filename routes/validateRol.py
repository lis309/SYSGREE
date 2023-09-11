from flask import render_template, session
from models.Modelos import Usuario


def verificarUsuario(rolRequerido):
    idUsuario = session.get('idUsuarioRolFK')
    if idUsuario:
        # Consulta la base de datos para obtener al usuario por su ID
        usuario = Usuario.query.get(idUsuario)     
        if usuario:
            # Verifica si el usuario tiene el rol requerido
            if usuario.rol == 1:
                # Si el usuario tiene el rol requerido, puedes acceder a sus atributos en tu vista
                return render_template('profile.html', usuario=usuario)
            elif usuario.rol == 2:
                # Si el usuario tiene el rol requerido, puedes acceder a sus atributos en tu vista
                return render_template('profile.html', usuario=usuario)
            else:
                # Manejar el caso en el que el usuario no tiene el rol requerido
                return "Acceso no autorizado", 403  # Devuelve un código de estado 403 (Prohibido), por ejemplo
        else:
            # Manejar el caso en el que el usuario no existe
            return "Usuario no encontrado", 404
    else:
        # Manejar el caso en el que el ID de usuario no está en la sesión
        return "Usuario no autenticado", 401  # Devuelve un código de estado 401 (No autorizado), por ejemplo


    