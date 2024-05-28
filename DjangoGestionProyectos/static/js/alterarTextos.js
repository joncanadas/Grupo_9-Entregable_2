  function aumentarTxt() {
    const txt = document.querySelectorAll('.contenedor')
    for (const t of txt) {
      const tamAct = parseFloat(t.style.fontSize) || 18 
      t.style.fontSize = `${tamAct + 2}px`
    }
  }
  
  function disminuirTxt() {
    const txt = document.querySelectorAll('.contenedor')
    for (const t of txt) {
      const tamAct = parseFloat(t.style.fontSize) || 18
      t.style.fontSize = `${tamAct - 2}px`
    }
  }
  
  document.getElementById('aumentarTxt').addEventListener('click', aumentarTxt)
  document.getElementById('disminuirTxt').addEventListener('click', disminuirTxt)
  


  