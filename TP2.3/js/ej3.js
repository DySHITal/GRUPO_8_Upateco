// Ejercicio 3
// Crear un vector de números con al menos 10 elementos, filtrar todos los números pares e
// insertarlo dentro de un elemento HTML.

let num = [1,2,3,4,5,6,7,8,9,10];
let numpar = num.filter(num => num % 2 === 0);  
const listaNumpar = document.getElementById('numPar');
numpar.forEach(num => {                        
    const item = document.createElement('li');
    item.textContent = num;
    listaNumpar.appendChild(item);
});