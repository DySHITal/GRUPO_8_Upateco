// Ejercicio 3
// Crear un vector de números con al menos 10 elementos, filtrar todos los números pares e 
// insertarlo dentro de un elemento HTML.

let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Filtro
const numerosPares = numeros.filter(numero => numero % 2 === 0);

// Elemento HTML
let numerosContainer = document.getElementById('numerosContainer');

const numerosPares2 = numerosPares.join(', ');

// Insertar en el elemento HTML
numerosContainer.textContent = `Números pares: ${numerosPares2}.`;
