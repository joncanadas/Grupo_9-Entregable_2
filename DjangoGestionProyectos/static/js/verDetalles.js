document.addEventListener("DOMContentLoaded", function () {
    // Supongamos que tienes varios botones, cada uno asociado con un proyecto
    var botones = document.querySelectorAll('.btnDetJS');

    // Añade un evento de clic a cada botón
    botones.forEach(boton => {
        boton.addEventListener('click', function() {
            var proyectoId = this.dataset.proyectoId;

            // Ahora puedes hacer la llamada fetch con este ID
            fetch('https://jsonplaceholder.typicode.com/users') // Esta es la URL de la API de nuestra aplicación, pero no encuentra los objetos `/api/proyecto/${proyectoId}/`
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