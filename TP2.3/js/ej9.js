// Crear un documento HTML con un formulario que contenga los campos Nombre y Email, se
// pide recuperar los valores ingresados y mostrarlos por consola.

const formulario = document.getElementById('formu');

formulario.addEventListener('submit', function(e){
    e.preventDefault();
    const datosFormulario = new FormData(formulario);
    const nombre = datosFormulario.get('name');
    const email = datosFormulario.get('email');

    console.log('Nombre: ', nombre);
    console.log('Email: ', email);
})