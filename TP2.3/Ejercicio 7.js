// Ejercicio 7
// Crear una función que oculte/muestre un div

const boton = document.getElementById("btn");
const ocultar = document.getElementById("ocultar");

let visibilidad = true;

boton.addEventListener('click', ()=>{
    if (visibilidad){
        ocultar.style.display = 'none';
        boton.textContent=`Mostrar`
    }
    else{
        ocultar.style.display='block';
        boton.textContent=`Ocultar`
    }
    visibilidad= !visibilidad;
 })