// Almacena los ingredientes seleccionados
var ingredientesSeleccionados = [];

function mostrarVentana(platoId, ventanaId) {
    return new Promise((resolve) => {
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
                    return [];
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

                        // Verificar si el checkbox está marcado y agregar al arreglo
                        if (checkbox.checked) {
                            ingredientesSeleccionados.push(ingrediente);
                        }

                        checkbox.addEventListener("change", function () {
                            // Actualiza el arreglo de ingredientes seleccionados al cambiar el estado del checkbox
                            if (this.checked) {
                                ingredientesSeleccionados.push(ingrediente);
                            } else {
                                // Remueve el ingrediente si el checkbox es deseleccionado
                                ingredientesSeleccionados = ingredientesSeleccionados.filter(function (item) {
                                    return item !== ingrediente;
                                });
                            }
                        });
                    });
                } else {
                    // Agregar los ingredientes a la lista sin checkboxes si es "ventanaIngredientes"
                    data.forEach(function (ingrediente) {
                        var li = document.createElement("li");
                        li.textContent = ingrediente;
                        listaIngredientes.appendChild(li);
                        // Agrega el ingrediente al arreglo inicialmente seleccionado
                        ingredientesSeleccionados.push(ingrediente);
                    });
                }

                // Mostrar la ventana emergente específica
                var ventana = document.getElementById(ventanaId);
                if (!ventana) {
                    console.error(`Elemento ${ventanaId} no encontrado.`);
                    resolve([]); // Resuelve la promesa con un arreglo vacío
                    return;
                }
                ventana.style.display = "block";

                // Resuelve la promesa con los ingredientes seleccionados
                resolve(ingredientesSeleccionados);
            });
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

var platoId;

document.querySelectorAll(".btn.btn-primary.mostrar-pedido").forEach(function(btn) {
    btn.addEventListener("click", function() {
        platoId = this.getAttribute("data-plato-id");
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


function manejarPedido() {
    // Obtén los valores del formulario
    var cantidad = document.getElementById('id_form-0-quantity').value;
    var metodoPago = document.querySelector('#ventanaPedido select').value;

    if (!metodoPago) {
        alert("Por favor, seleccione un método de pago.");
        return;
    }

    // Crea un objeto con los datos del pedido
    var datosPedido = {
        plato_id: platoId,
        cantidad: parseInt(cantidad),
        ingredientes: ingredientesSeleccionados,
        metodo_pago: metodoPago
    };

    // Realiza la solicitud AJAX al backend
    fetch('/realizar_pedido', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datosPedido)
    })
    .then(response => response.json())
    .then(data => {
        alert("Su pedido ya fue generado!!");
        // Recargar la página después de 1 segundo (1000 milisegundos)
        setTimeout(function() {
            location.reload();
        }, 1000);
    })
    .catch(error => console.error('Error:', error));
}

// Manejar el pedido cuando se hace clic en el botón de "Pedir"
document.getElementById("btnPedir").addEventListener("click", function() {
    manejarPedido();
})