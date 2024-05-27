document.addEventListener("DOMContentLoaded", function () {
  
  var infoBlock = document.getElementById("info-block");
  infoBlock.style.display = "none"; // Ocultar el bloque de información inicialmente

  // Capturar el evento de clic en el botón para expandir información
  document
    .getElementById("expand-button")
    .addEventListener("click", function () {
      var infoBlock = document.getElementById("info-block");

      if (infoBlock.style.display === "none") {
        infoBlock.style.display = "block"; // Mostrar el bloque
        this.innerHTML = "Ocultar información"; // Cambiar el texto del botón
      } else {
        infoBlock.style.display = "none"; // Ocultar el bloque
        this.innerHTML = "Bienvenido a Deustotil Tech S.L.<br><br>(Más información)"; // Cambiar el texto del botón
      }
    });
});
