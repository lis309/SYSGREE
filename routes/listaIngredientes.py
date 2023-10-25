"""
from flask_sqlalchemy import SQLAlchemy
from models import IngredientePlato, Ingrediente, Plato

# ...

# Realizar INNER JOIN entre Ingrediente, Plato e IngredientePlato
result = db.session.query(Ingrediente.nombre, Plato.nombre).join(
    IngredientePlato, IngredientePlato.codigoIngredienteFK == Ingrediente.codigoIngrediente
).join(Plato, IngredientePlato.codigoPlatoFK == Plato.codigoPlato).all()

# Procesar los resultados y devolver los nombres de los ingredientes en formato JSON
ingredientes = [ingrediente for ingrediente, plato in result]

# Devolver los nombres de los ingredientes en formato JSON
return jsonify(ingredientes)

"""

"""
<!DOCTYPE html>
<html>
<head>
  <!-- Otros elementos head -->
</head>
<body>
  <button id="mostrarVentana">Mostrar Ventana Emergente</button>

  <div id="ventanaEmergente" class="ventana">
    <div class="contenido">
      <span class="cerrar" id="cerrarVentana" onclick="cerrarVentana()">&times;</span>
      <h2>Lista de Ingredientes</h2>
      <div id="jsonContainer"></div>
    </div>
  </div>

  <script>
    document.getElementById("mostrarVentana").addEventListener("click", function () {
      mostrarVentana();
    });

    function mostrarVentana() {
      // Realizar una solicitud AJAX para obtener el JSON de la ruta del backend
      fetch("/platos_ingredientes")  // Reemplaza esto con la URL correcta de tu ruta
        .then(response => response.json())
        .then(data => {
          // Mostrar el JSON en el div
          document.getElementById("jsonContainer").textContent = JSON.stringify(data, null, 2);
        });

      // Mostrar la ventana emergente
      document.getElementById("ventanaEmergente").style.display = "block";
    }

    function cerrarVentana() {
      document.getElementById("ventanaEmergente").style.display = "none";
    }
  </script>
</body>
</html>

"""
"""
/* Estilos generales */
body {
    font-family: Arial, sans-serif;
}

/* Estilos del botón de mostrar ventana emergente */
#mostrarVentana {
    padding: 10px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    cursor: pointer;
}

/* Estilos de la ventana emergente */
.ventana {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
}

/* Estilos del contenido de la ventana emergente */
.contenido {
    background-color: #fff;
    width: 70%;
    max-width: 600px;
    margin: 100px auto;
    padding: 20px;
    border: 1px solid #333;
    border-radius: 5px;
    position: relative;
}

/* Estilos del botón de cierre (la "X") */
.cerrar {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 20px;
    cursor: pointer;
    color: #333;
}

/* Estilos para el título de la ventana emergente */
h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

/* Estilos para el contenedor del JSON */
#jsonContainer {
    font-family: monospace;
    white-space: pre;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f7f7f7;
    overflow: auto;
}

"""