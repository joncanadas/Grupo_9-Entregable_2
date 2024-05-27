const emailInput = document.getElementById('email');

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