// Ejercicio 7
// Crear una función que oculte/muestre un div.

const hidden = document.getElementById('hidden');
const boton = document.getElementById('btn');
let visible = true;

boton.addEventListener('click', function(){
    if(visible){
        hidden.style.opacity = '1';
        visible = false;
    } else{
        hidden.style.opacity = '0';
        visible = true;
    }
})