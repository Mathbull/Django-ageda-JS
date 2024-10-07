document.addEventListener("DOMContentLoaded", function (){
    let buttonRegister = document.getElementById("buttonRegister");
    let buttonReturn_login = document.getElementById("buttonReturn_login")

    if(buttonRegister){
        buttonRegister.addEventListener('click', function(){
            window.location.href= '/register';
        })
    }

    if(buttonReturn_login){
        buttonReturn_login.addEventListener('click', function(){
            window.location.href= '/login';
        })
    }

})