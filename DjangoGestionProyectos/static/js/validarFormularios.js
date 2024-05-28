const formularioCrearPre = document.getElementById('formularioCrP');
const formularioModifPre = document.getElementById('formularioMdfP');
const nombrePro = document.getElementById('nombrePro');

(function () {

  formularioCrearPre.addEventListener('submit', function (e) {
    let nombrePro = String(Presupuesto.value).trim
    if(nombrePro.length < 8){
      alert("Pruebbaaaa")
      e.preventDefault()
    }
  })
  
  formularioModifPre.addEventListener('submit', function (e) {
    let presupuesto = Dec(Presupuesto.value)
    if(presupuesto < 0.00){
      alert("Pruebbaaaa")
      e.preventDefault()
    }
  })

})




function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

emailInput.addEventListener('oninput', () => {
  const email = emailInput.value;
  const errorSpan = document.getElementById('email-error');

  if (validateEmail(email)) {
    errorSpan.style.display = 'none';
  } else {
    errorSpan.style.display = 'block';
    errorSpan.textContent = 'Correo electrónico no válido';
  }
});