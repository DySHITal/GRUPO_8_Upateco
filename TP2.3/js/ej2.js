// Ejercicio 2
// Escribe una función que tome un array de números como parámetro y devuelva un nuevo
// array con los números ordenados de forma ascendente.

function ordenarArr(arr) {
    long = arr.length
    let parar;
    do {
      parar = false;
      for (let i = 0; i < long - 1; i++) {
        if (arr[i] > arr[i + 1]) {
          const aux = arr[i];
          arr[i] = arr[i + 1];
          arr[i + 1] = aux;
          parar = true;
        }
      }
      long--;
    } while (parar);
    return arr;
  }
  
  const arr = [3, 4, 1, 8];
  console.log(ordenarArr(arr));
  