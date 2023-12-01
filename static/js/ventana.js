function mostrarVentana(platoId, ventanaId) {
    // Realizar una solicitud AJAX para obtener los ingredientes del plato
    fetch(`/obtener_ingredientes?id=${platoId}`)
        .then(response => response.json())
        .then(data => {
            // Limpiar la lista de ingredientes específica
            var listaIngredientes;
            if (ventanaId === "ventanaIngredientes") {
                listaIngredientes = document.getElementById("listaIngredientes");
            } else if (ventanaId === "ventanaPedido") {
                listaIngredientes = document.getElementById("listaIngredientesPedido");
            }

            if (!listaIngredientes) {
                console.error(`Elemento listaIngredientes${ventanaId} no encontrado.`);
                return;
            }

            listaIngredientes.innerHTML = "";

            // Agregar los ingredientes a la lista con checkboxes solo si es "ventanaPedido"
            if (ventanaId === "ventanaPedido") {
                data.forEach(function (ingrediente) {
                    var checkbox = document.createElement("input");
                    checkbox.type = "checkbox";
                    checkbox.checked = true; // Establecer como seleccionado por defecto
                    checkbox.value = ingrediente;
                    checkbox.classList.add("checkbox-ingredientes"); // Agregar clase al checkbox

                    var label = document.createElement("label");
                    label.appendChild(document.createTextNode(ingrediente));
                    label.classList.add("label-ingredientes"); // Agregar clase al label

                    var listItem = document.createElement("li");
                    listItem.appendChild(checkbox);
                    listItem.appendChild(label);

                    listaIngredientes.appendChild(listItem);
                });
            } else {
                // Agregar los ingredientes a la lista sin checkboxes si es "ventanaIngredientes"
                data.forEach(function (ingrediente) {
                    var li = document.createElement("li");
                    li.textContent = ingrediente;
                    listaIngredientes.appendChild(li);
                });
            }

            // Mostrar la ventana emergente específica
            var ventana = document.getElementById(ventanaId);
            if (!ventana) {
                console.error(`Elemento ${ventanaId} no encontrado.`);
                return;
            }
            ventana.style.display = "block";
        });
}

function realizarPedido() {
    var platoId = document.getElementById("plato_id_pedido").value;
    var cantidad = document.getElementById("quantity_pedido").value;
    var valorPedido = document.getElementById("valor_pedido").value;
    var metodoPago = document.getElementById("metodo_pago").value;

    // Obtén la lista de ingredientes (como en el ejemplo anterior)

    // Construye el objeto que se enviará al servidor
    var pedidoData = {
        id: platoId,
        ingredientes: listaIngredientes,
        cantidad: cantidad,
        metodo_pago: metodoPago,
        valorPedido: valorPedido
    };

    // Realiza la solicitud POST al servidor
    fetch('/insertar_pedido', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(pedidoData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        // Puedes realizar acciones adicionales después de la inserción, si es necesario
    })
    .catch(error => {
        console.error('Error al insertar pedido:', error);
    });
}

function cerrarVentana(ventanaId) {
    var ventana = document.getElementById(ventanaId);
    ventana.style.display = "none";
}

document.querySelectorAll(".btn.btn-primary.mostrar-ingredientes").forEach(function(btn) {
    btn.addEventListener("click", function() {
        var platoId = this.getAttribute("data-plato-id");
        mostrarVentana(platoId, "ventanaIngredientes");
    });
});

document.querySelectorAll(".btn.btn-primary.mostrar-pedido").forEach(function(btn) {
    btn.addEventListener("click", function() {
        var platoId = this.getAttribute("data-plato-id");
        mostrarVentana(platoId, "ventanaPedido");
    });
});

// Agregar eventos para cerrar ventanas
document.getElementById("cerrarVentanaIngredientes").addEventListener("click", function() {
    cerrarVentana("ventanaIngredientes");
});

document.getElementById("cerrarVentanaPedido").addEventListener("click", function() {
    cerrarVentana("ventanaPedido");
});
