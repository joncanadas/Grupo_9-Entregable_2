document.addEventListener("DOMContentLoaded", function () {
    // Supongamos que tienes varios botones, cada uno asociado con un proyecto
    var botones = document.querySelectorAll('.btnDetJS');

    // Añade un evento de clic a cada botón
    botones.forEach(boton => {
        boton.addEventListener('click', function() {
            // Cuando se hace clic en un botón, obtén el ID del proyecto de un atributo de datos
            var proyectoId = this.dataset.proyectoId;

            // Ahora puedes hacer la llamada fetch con este ID
            fetch(`/api/proyecto/${proyectoId}/`)
                .then(response => response.json())
                .then(data => {
                    // Aquí tienes los datos del proyecto
                    console.log(data);
                    // Ahora puedes usar estos datos para modificar el DOM
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
});