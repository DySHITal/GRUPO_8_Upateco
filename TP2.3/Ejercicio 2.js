// Ejercicio 2
// Escribe una función que tome un array de números como parámetro y devuelva un nuevo 
// array con los números ordenados de forma ascendente.
function ordenarAscendente(arrayNumeros) {
    return arrayNumeros.sort((a, b) => a - b);
  }
  
   
  const numeros = [10, 4, 8, 2, 6];
  ordenarAscendente(numeros);
  console.log(numeros); 
  