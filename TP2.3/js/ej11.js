// Ejercicio 11
// Crea un calendario simple que muestre los eventos programados para un día específico.
// Puedes usar objetos para representar los eventos y mostrarlos en una lista.

const eventos = [
    {
      hora: '07:00',
      descripcion: 'Entrada laboral',
      lugar: 'Empresa'
    },
    {
      hora: '18:00',
      descripcion: 'Salida laboral',
      lugar: 'Empresa'
    },
    {
      hora: '20:00',
      descripcion: 'Clase de programación',
      lugar: 'Online'
    }
  ];
  
  function mostrarEventos() {
    const calendario = document.getElementById('calendario');
    const lista = document.createElement('ul');
  
    eventos.forEach(evento => {
      const item = document.createElement('li');
      item.innerHTML = `
        <b>Hora:</b> ${evento.hora}<br>
        <b>Descripción:</b> ${evento.descripcion}<br>
        <b>Lugar:</b> ${evento.lugar}
      `;
      lista.appendChild(item);
    });
  
    if (eventos.length === 0) {
      const nada = document.createElement('p');
      nada.textContent = 'No hay eventos para este día.';
      lista.appendChild(nada);
    }
  
    calendario.appendChild(lista);
  }
  
  mostrarEventos();