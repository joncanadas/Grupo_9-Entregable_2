const footer = {
    nombre : 'Amaia',
    apellidos : 'Jainaga Urrutia',
    edad : 27,
    email : 'amaia@email.com',
}


function crearElemento(label, valor) {
    return `<li>${label} : ${valor}</li>`;
}

function crearLista(objeto){
    let lista = '<ul>'
    for(const key in objeto){
        console.log(key); // Clave
        console.log(objeto[key]); // Valor
        lista += crearElemento(key, objeto[key]); // estudiante["nombre"]
    }
    lista += '</ul>'
    return lista;
}

let listaHTML = crearLista(footer);
document.getElementById('footer').insertAdjacentHTML('afterbegin', listaHTML);
//document.getElementById('lista').innerHTML = listaHTML;

//En base a este html

/*
<footer class="site-footer">
        <div class="grid-footer contenedor">
            <nav class="footer-menu">
                <a href="#">Dirección:</a>
                <a href="#">Calle del Dron, 12 <br> 01001
                    Vitoria-Gasteiz, Álava</a>
                <a href="#">Teléfono:</a>
                <a href="#">+34 945 123 456</a>
            </nav>
        </div>

        <p class="copyright">Derechos reservados a
            <span>BrumaDron</span></p>
    </footer>
*/