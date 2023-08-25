// Ejercicio 4
// Encontrar el número más grande en un Array.

function encontrarMayor(arreglo){
    let mayor = arreglo[0];
    
    for (let i=1;i < arreglo.lenght; i++){
        if (arreglo[i]>mayor){
            mayor=arreglo[i];
        }
    }
    return mayor;
}

const numeros = [25, 10, 45, 30, 5];
console.log(encontrarMayor(numeros));