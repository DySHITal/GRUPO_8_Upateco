// Ejercicio 6
// Crea un botón y agregarle un evento para que cambie de color.

//obtengo elementos
const boton = document.getElementById("btn");
const contador= document.getElementById("contar")
//Elemento no requerido
let cuenta=0

//se crea evento de click
boton.addEventListener("click", () =>{
    //Creo arreglo de colores
    const colores = ['red', 'green', 'blue', 'purple', 'orange'];
    //se elige aleatoriamente el color
  const colorAleatorio = colores[Math.floor(Math.random() * colores.length)];
  //Se cambia el color del boton
  boton.style.backgroundColor = colorAleatorio;
  //contador extra
  cuenta=cuenta+1;
  contador.textContent=`${cuenta}`;
})
