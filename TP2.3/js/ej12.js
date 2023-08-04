// Ejercicio 12
// Crear un “chatBox” donde tome los datos de un input y los muestre, (Se debe usar HTML,
// CSS y JavaScript).


function mostrarMensaje(){
    const chat = document.getElementById('formu');
    const listaChat = document.getElementById('msgs')
    
    chat.addEventListener('submit', function(e){
        e.preventDefault();
        const datoMensaje = new FormData(chat);
        const mensaje = datoMensaje.get('mensaje');
        const item = document.createElement('li');
        item.innerHTML = `
        <p class="chat">${mensaje}</p>
        `;
        listaChat.appendChild(item);
        chat.reset();
    });
    
}

mostrarMensaje();