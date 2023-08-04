// Ejercicio 5
// Escribe una función que tome un número como parámetro y calcule la suma de todos los
// números primos menores o iguales a ese número.

function esPrimo(numero) {
    if (numero <= 1) {
      return false;
    }
    
    for (let i = 2; i <= Math.sqrt(numero); i++) {
      if (numero % i === 0) {
        return false;
      }
    }
  
    return true;
  }
  
  function sumaPrimos(numero) {
    let suma = 0;
    for (let i = 2; i <= numero; i++) {
      if (esPrimo(i)) {
        suma += i;
      }
    }
  
    return suma;
  }
  
  const numero = 10; // Cambia este número para obtener la suma de primos menores o iguales a un número diferente
  console.log('La suma de números primos menores o iguales a', numero, 'es:', sumaPrimos(numero));
  