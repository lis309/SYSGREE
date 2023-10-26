document.addEventListener("DOMContentLoaded", () => {
    const searchButton = document.getElementById("searchButton");
    const searchInput = document.getElementById("searchInput");
    const resultsDiv = document.getElementById("results");

    searchButton.addEventListener("click", () => {
        const searchTerm = searchInput.value;

        // Realiza una solicitud al servidor para buscar platos
        fetch(`/buscar?nombre=${searchTerm}`)
            .then(response => response.json())
            .then(data => {
                resultsDiv.innerHTML = "";

                if (data.length > 0) {
                    data.forEach(plato => {
                        const row = document.createElement("tr");
                        row.innerHTML = `
                            <td>${plato.codigoPlato}</td>
                            <td>${plato.nombrePlato}</td>
                            <td>${plato.descripcionPlato}</td>
                            <td>${plato.precioPlato}</td>
                            <td><a href="${plato.url_actualizar}" class="boton">Actualizar</a></td>
                            <td><a href="${plato.url_eliminar}" class="boton boton-rojo">Eliminar</a></td>
                        `;
                        resultsDiv.querySelector("tbody").appendChild(row);
                    });
                } else {
                    resultsDiv.innerHTML = "<p>No se encontraron resultados.</p>";
                }
            });
    });
});
