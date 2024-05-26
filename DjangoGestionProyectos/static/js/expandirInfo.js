document.addEventListener("DOMContentLoaded", function () {
  // Capturar el evento de clic en el botón para expandir información
  document
    .getElementById("expand-button")
    .addEventListener("click", function () {
      var infoBlock = document.getElementById("info-block");

      if (infoBlock.style.display === "none") {
        infoBlock.style.display = "block"; // Mostrar el bloque
        this.textContent = "Ocultar información"; // Cambiar el texto del botón
      } else {
        infoBlock.style.display = "none"; // Ocultar el bloque
        this.textContent = "Expandir información"; // Cambiar el texto del botón
      }
    });
});
