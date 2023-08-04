// Ejercicio 4
// Encontrar el número más grande en un Array.

function mayor(arr){
    long = arr.length
    let mayor = arr[0];
    for(i=1; i < long; i++){
        if(arr[i]>mayor){
            mayor = arr[i];
        }
    }
    return mayor;
}

let arr = [6,5,4,3,2,8];
console.log('El numero mas grande del array es: ' + mayor(arr));