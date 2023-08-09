// Ejercicio 9
// Crear un documento HTML con un formulario que contenga los campos Nombre y Email, se 
// pide recuperar los valores ingresados y mostrarlos por consola.

const formulario = document.getElementById("formulario") ;

addEventListener('submit', function(event) {
    event.preventDefault(); //No se envia el formulario
    //caso contrario no podria guardar los datos al hacer click en submit

      const nombre = formulario.nombre.value;
      const email = formulario.email.value;

      console.log(`Nombre: ${nombre}`)
      console.log(`Email: ${email}`)

})