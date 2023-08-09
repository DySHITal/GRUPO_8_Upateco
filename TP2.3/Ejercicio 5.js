// Ejercicio 5
// Escribe una función que tome un número como parámetro y calcule la suma de todos los 
// números primos menores o iguales a ese número.

function esPrimo(num) {
    if (num <= 1) {
      return false;
    }
    if (num <= 3) {
      return true;
    }
    if (num % 2 === 0 || num % 3 === 0) {
      return false;
    }
    for (let i = 5; i * i <= num; i += 6) {
      if (num % i === 0 || num % (i + 2) === 0) {
        return false;
      }
    }
    return true;
  }

function sumaDePrimos(numero){
    let suma=0;

    for(let i=1; i<=numero; i++){
        if (esPrimo(i)){
            suma=suma+i;
        }
    }
    return suma;
}
let numero = 10;
let suma =sumaDePrimos(numero);
console.log(`Suma de números primos menores o iguales a ${numero} es: ${suma}`);