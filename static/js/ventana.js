document.querySelectorAll(".btn.btn-primary.mostrar-ventana").forEach(function(btn) {
    btn.addEventListener("click", function() {
        var platoId = this.getAttribute("data-plato-id");
        mostrarVentana(platoId);
    });
});

function mostrarVentana(platoId) {
    console.log("Función mostrarVentana llamada con platoId: " + platoId);
    // Realizar una solicitud AJAX para obtener los ingredientes del plato
    fetch(`/obtener_ingredientes?id=${platoId}`)
        .then(response => response.json())
        .then(data => {
            // Limpiar la lista de ingredientes
            var listaIngredientes = document.getElementById("listaIngredientes");
            listaIngredientes.innerHTML = "";
            
            // Agregar los ingredientes a la lista
            data.forEach(function(ingrediente) {
                var li = document.createElement("li");
                li.textContent = ingrediente;
                listaIngredientes.appendChild(li);
            });
        });

    // Mostrar la ventana emergente
    document.getElementById("ventanaEmergente").style.display = "block";
}

function cerrarVentana() {
    document.getElementById("ventanaEmergente").style.display = "none";
}

document.querySelectorAll(".btn.btn-primary.mostrar-pedido").forEach(function(btn) {
    btn.addEventListener("click", function() {
        var platoId = this.getAttribute("data-plato-id");
        mostrarVentana2(platoId);
    });
});

function mostrarVentana2(platoId) {
    console.log("Función mostrarVentana2 llamada con platoId: " + platoId);
    // Realizar una solicitud AJAX para obtener los ingredientes del plato
    fetch(`/obtener_ingredientes?id=${platoId}`)
        .then(response => response.json())
        .then(data => {
            // Limpiar la lista de ingredientes
            var listaIngredientes = document.getElementById("listaIngredientes");
            listaIngredientes.innerHTML = "";
            
            // Agregar los ingredientes a la lista
            data.forEach(function(ingrediente) {
                var li = document.createElement("li");
                li.textContent = ingrediente;
                listaIngredientes.appendChild(li);
            });
        });

    // Mostrar la ventana emergente
    document.getElementById("ventanaEmergente").style.display = "block";
}

function cerrarVentana() {
    document.getElementById("ventanaEmergente").style.display = "none";
}
