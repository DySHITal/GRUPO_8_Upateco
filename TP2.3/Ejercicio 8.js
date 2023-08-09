// Ejercicio 8
// Crear un objeto persona que contenga nombre, apellido, edad, sexo y teléfono. Luego crear 
// una tabla (con JavaScript) e insertar los datos con su respectivo encabezado.

//funcion de crear personas, por si despues quiero agregar mas
function Persona(nombre, apellido,edad, sexo,telefono){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad=edad;
        this.sexo=sexo;
        this.telefono=telefono;
        };
//Creo a mi persona 1, de crear mas podria guardarlas en un dic o array
let persona1=new Persona("Javier","Garcia",27,"masc", 12345678);
//Obtengo el elemento tabla
const tabla = document.getElementById("tabla");
const cuerpoTabla = tabla.querySelector("tbody");

const fila = document.createElement("tr");

fila.innerHTML=`<th>${persona1.nombre}</th>
                 <th>${persona1.apellido}</th>
                 <th>${persona1.edad}</th>
                 <th>${persona1.sexo}</th>
                 <th>${persona1.telefono}</th>`;

cuerpoTabla.appendChild(fila);
        