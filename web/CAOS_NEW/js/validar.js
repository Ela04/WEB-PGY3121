const nombre = document.getElementById("usuario")
const contra = document.getElementById("password")
const mail = document.getElementById("correo")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    if (nombre.nodeValue.length <3) {
        warnings += "Nombre muy corto"
    }
})