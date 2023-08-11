// Ejercicio 12
// Crear un “chatBox” donde tome los datos de un input y los muestre, (Se debe usar HTML, 
// CSS y JavaScript).

const chatBox = document.getElementById('chatBox');
const mensajeInput = document.getElementById('mensajeInput');
const enviarBtn = document.getElementById('enviarBtn');

enviarBtn.addEventListener('click', () => {
  const mensaje = mensajeInput.value;

  if (mensaje.trim() !== '') {
    const mensajeElement = document.createElement('div');
    mensajeElement.classList.add('mensaje');
    mensajeElement.textContent = mensaje;

    chatBox.appendChild(mensajeElement);

    mensajeInput.value = '';
  }
});
