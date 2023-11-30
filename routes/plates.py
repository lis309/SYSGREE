# Importar flask y otros metodos
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar mi modelo
from models.Modelos import Plato

# Conexion a la bd
from utils.db import db

#Importar el decorador
from .validateRol import usuarioAdminRequired
from .logout import cerrarSesion
from sqlalchemy.exc import IntegrityError

plates = Blueprint("plates", __name__)

@plates.route("/listarPlato")
@usuarioAdminRequired
@cerrarSesion
def consultarPlato():
    plates = Plato.query.all()
    return render_template("plato/Consultar_Plato.html", plates=plates)


@plates.route("/registrarPlato")
@usuarioAdminRequired
@cerrarSesion
def capturarPlato():
    return render_template("plato/RegistrarPlato.html")

@plates.route("/registrarPlate", methods=["POST"])
@usuarioAdminRequired
@cerrarSesion
def registrarPlato():
    nombre = request.form.get("nombre")
    descripcion = request.form.get("descripcion")
    precio = request.form.get("precio")
    
    estado = "Activo" 

    nuevoPlato = Plato(nombre, descripcion, precio, estado)

    db.session.add(nuevoPlato)
    db.session.commit()
    
    flash("El plato se registró correctamente", "success")

    return redirect(url_for("plates.consultarPlato"))


@plates.route("/actualizarPlato/<codigoPlato>", methods=["POST", "GET"])
@usuarioAdminRequired
@cerrarSesion
def actualizarPlato(codigoPlato):

    plate = Plato.query.get(codigoPlato)

    if request.method == "POST":
        plate.nombrePlato = request.form["nombre"]
        plate.descripcionPlato = request.form["descripcion"]
        plate.precioPlato = request.form["precio"]

        db.session.commit()
        
        flash("El ingrediente se actualizó correctamente", "success")
        
        return redirect(url_for("plates.consultarPlato"))

    return render_template("plato/ActualizarPlato.html", plate=plate)


@plates.route("/eliminarPlato/<int:codigoPlato>", methods=['POST'])
@usuarioAdminRequired
@cerrarSesion
def eliminarPlato(codigoPlato):
    try:
        plate = Plato.query.get(codigoPlato)

        if plate:
            # Actualiza el campo 'estado' en lugar de eliminar físicamente
            plate.estadoPlato = ("Inactivo")
            db.session.commit()
            flash("El plato se eliminó correctamente", "success")
            return jsonify({'message': 'Plato eliminado con éxito'})
        else:
            flash("No se pudo encontrar el plato a eliminar", "error")
            return jsonify({'message': 'Error al eliminar el plato'})
    except IntegrityError as e:
        # Si hay una violación de la clave externa, maneja el error
        db.session.rollback()
        flash(f"No se puede eliminar el plato debido a restricciones de integridad referencial: {str(e)}", "error")
        return jsonify({'message': f'Error al eliminar el plato debido a restricciones de integridad referencial: {str(e)}'})


@plates.route("/buscarPlato")
@usuarioAdminRequired
@cerrarSesion
def buscar_platos():
    search_term = request.args.get("nombre").lower()
    resultados = Plato.query.filter(Plato.nombrePlato.ilike(f"%{search_term}%")).all()
    resultados = [{"id": plato.id, "nombrePlato": plato.nombrePlato} for plato in resultados]
    return jsonify(resultados)
