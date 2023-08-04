

const tabla = document.getElementById('tabla');
const tbody = tabla.getElementsByTagName('tbody')[0];

function nombreSplit(fullname){
    const nombre = fullname.split(' ')
    return nombre[0]
}

function apellidoSplit(fullname){
    const apellido = fullname.split(' ')
    return apellido[1]
}

function crearUsuario(usuario){
    const fila = document.createElement('tr');
    fila.innerHTML = `
        <td>${nombreSplit(usuario.name)}</td>
        <td>${apellidoSplit(usuario.name)}</td>
        <td>${usuario.email}</td>
        <td>${usuario.company.name}</td>
        <td>${usuario.address.street + ' ' + usuario.address.suite}</td>`;
    return fila;
}


fetch('https://jsonplaceholder.typicode.com/users')
.then(response => response.json())
.then(data => {
    data.forEach(usuario => {
        const filaUsuario = crearUsuario(usuario);
        tbody.appendChild(filaUsuario)     
    });
})
.catch(error => {
    console.error('Error:', error);
});

