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
      pro: 1,
      cliente : 'Tesla',
      descripcion : 'Proyecto de autoreparación'
  },
  {
      pro: 2,
      cliente : 'Nasa',
      descripcion : 'Proyecto de gestión de coordenadas'
  },
  {
      pro: 3,
      cliente : 'FiFa',
      descripcion : 'Proyecto de control de expedientes'
  }
];

function crearInfo(pro, cliente, descripcion){
  return `
      <tr>
          <td>${pro}</td>
          <td>${cliente}</td>
          <td>${descripcion}</td>
      </tr>`;
}

function crearTablaInformacion(informacion) {
  let tabla = `
      <table>
          <thead>
              <tr>
                  <td>Proyectos más importantes</td>
                  <td>Cliente</td>
                  <td>Descripción</td>
              </tr>
          </thead>
          <tbody>
  `;

  // Recorrer el listado de tareas para crear una fila por cada tarea
  for(const info of informacion) {
      tabla += crearInfo(info.pro, info.cliente, info.descripcion)
  }
  tabla += '</tbody></table>'
  return tabla;
}

let tabla = crearTablaInformacion(informacion)
document.getElementById('contenedor-informacion').innerHTML = tabla