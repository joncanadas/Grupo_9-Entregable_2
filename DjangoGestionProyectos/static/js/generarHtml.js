function generarFooter() {
    const footer = document.createElement('footer');
    footer.classList.add('site-footer');
  
    const contenedor = document.createElement('div');
    contenedor.classList.add('grid-footer', 'contenedor');
  
    const nav = document.createElement('nav');
    nav.classList.add('footer-menu');
  
    const direccionTit = document.createElement('a');
    direccionTit.textContent = 'Dirección:';
  
    const direccionCalle = document.createElement('a');
    direccionCalle.textContent = 'Calle Arriagako Atea, 62\n01013 Vitoria-Gasteiz, Álava';

    const telefonoTit = document.createElement('a');
    telefonoTit.textContent = 'Teléfono:';
  
    const telefonoNum = document.createElement('a');
    telefonoNum.textContent = '+34 945 123 456';
  
    nav.appendChild(direccionTit);
    nav.appendChild(direccionCalle);
    nav.appendChild(telefonoTit);
    nav.appendChild(telefonoNum);
  
    contenedor.appendChild(nav);
    footer.appendChild(contenedor);
  
    const copyright = document.createElement('p');
    copyright.classList.add('copyright');
    copyright.textContent = 'Derechos reservados por ';
  
    const span = document.createElement('span');
    span.textContent = 'Deustotil Tech S.L.';
    copyright.appendChild(span);
  
    footer.appendChild(copyright);
  
    return footer;
  }

  const footerElement = document.getElementById('contenedor-footer');
  footerElement.appendChild(generarFooter());

const informacion = [
  {
      cliente : 'Tesla',
      descripcion : 'Proyecto de autoreparación'
  },
  {
      cliente : 'Nasa',
      descripcion : 'Proyecto de gestión de coordenadas'
  },
  {
      cliente : 'FiFa',
      descripcion : 'Proyecto de control de expedientes'
  }
];

function crearElemento(label, valor) {
  return `<ol>${label} : ${valor}</ol>`;
}

function crearLista(informacion){
  let lista = '<ul>'
  for(const key in informacion){
      console.log(key); 
      console.log(informacion[key]); 
      lista += crearElemento(key, informacion[key]); 
  }
  lista += '</ul>'
  return lista;
}

let listaHTML = crearLista(informacion);
document.getElementById('contenedor-informacion').insertAdjacentHTML('afterbegin', listaHTML);
