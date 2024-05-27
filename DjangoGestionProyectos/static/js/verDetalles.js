document.addEventListener("DOMContentLoaded", function () {
    // Supongamos que tienes varios botones, cada uno asociado con un proyecto
    var botones = document.querySelectorAll('.btnDetJS');

    // Añade un evento de clic a cada botón
    botones.forEach(boton => {
        boton.addEventListener('click', function() {
            var proyectoId = this.dataset.proyectoId;

            // Ahora puedes hacer la llamada fetch con este ID
            fetch('https://jsonplaceholder.typicode.com/users') // URL original: `/api/proyecto/${proyectoId}/`
                .then(response => response.json())
                .then(data => {
                    // Aquí tienes los datos del proyecto
                    console.log(data);
                    var proyectoInfo = document.getElementById(`proyecto-${proyectoId}-info`);

                    // Crea el contenido HTML con los datos del proyecto
                    var contenido = `
                      <h2>${data.name}</h2>
                      <p>${data.email}</p>
                      <p>${data.phone}</p>
                    `;

                     // Asigna el contenido al div
                     proyectoInfo.innerHTML = contenido;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
});