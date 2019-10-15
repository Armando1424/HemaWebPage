function validarRegister(){

    var nickName, userName, firstLastname, secondLastname, email, password, exprecion; 
    nickName = document.getElementById("nickName").value;
    userName = document.getElementById("userName").value;
    firstLastname = document.getElementById("firstLastname").value;
    secondLastname = document.getElementById("secondLastname").value;
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;

    exprecion = "/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/";

    if( nickName === ""){
        alert("El campo nombre clave esta vacio");
        return false;
    }else if( nickName.legth > 200){
        alert("El nombre clave es muy largo");
        return false;
    }else if( userName === ""){
        alert("El campo nombre esta vacio");
        return false;
    }else if( userName.legth > 200){
        alert("El nombre es muy largo");
        return false;
    }else if( firstLastname === ""){
        alert("El campo primer apellido esta vacio");
        return false;
    }else if( firstLastname.legth > 200){
        alert("El primer apellido es muy largo");
        return false;
    }else if( secondLastname === ""){
        alert("El campo segundo apellido esta vacio");
        return false;
    }else if( secondLastname.legth > 200){
        alert("El segundo apellido es muy largo");
        return false;
    }else if( email === ""){
        alert("El campo correo electronico esta vacio");
        return false;
    }else if( email.legth > 200){
        alert("El correo es muy largo");
        return false;
    }else if( !exprecion.test(email) ){
        alert("El correo no es valido");
        return false;
    }else if( password === ""){
        alert("El campo contraseña esta vacio");
        return false;
    }else if( password.legth > 200){
        alert("La contraseña es muy largo");
        return false;
    }

}

function validarLogin(){

    var email, password, exprecion;
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;

    exprecion = "/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/";

    if( email === ""){
        alert("El campo correo electronico esta vacio");
        return false;
    }else if( email.legth > 200){
        alert("El correo es muy largo");
        return false;
    }else if( !exprecion.test(email) ){
        alert("El correo no es valido");
        return false;
    }else if( password === ""){
        alert("El campo contraseña esta vacio");
        return false;
    }else if( password.legth > 200){
        alert("La contraseña es muy largo");
        return false;
    }

}