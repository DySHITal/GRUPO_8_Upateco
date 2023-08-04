// Ejercicio 8
// Crear un objeto persona que contenga nombre, apellido, edad, sexo y teléfono. Luego crear
// una tabla (con JavaScript) e insertar los datos con su respectivo encabezado.

const persona = {
    nombre: 'Alfredo',
    apellido: 'Moreno',
    edad: 37,
    sexo: 'Masculino',
    telefono: 115487953
}

const tabla = document.getElementById('tabla');

tabla.innerHTML = `<table border = '1'>
                        <tr>
                            <th>Nombre</th>
                            <th>Apellido</th>
                            <th>Edad</th>
                            <th>Sexo</th>
                            <th>Teléfono</th>
                        </tr>
                        <tr>
                            <td>${persona.nombre}</td>
                            <td>${persona.apellido}</td>
                            <td>${persona.edad}</td>
                            <td>${persona.sexo}</td>
                            <td>${persona.telefono}</td>
                        </tr>
                    </table>`
