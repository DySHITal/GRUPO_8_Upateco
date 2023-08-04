// Ejercicio 6
// Crea un botón y agregarle un evento para que cambie de color.
let colorOriginal = true;
const boton = document.getElementById('btn');
boton.addEventListener('click', function(){
    if(colorOriginal){
        boton.style.backgroundColor = 'lightblue';
        colorOriginal = false;
    } else {
        boton.style.backgroundColor = '';
        colorOriginal = true;
    }
})