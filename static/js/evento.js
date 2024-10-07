document.addEventListener("DOMContentLoaded", function (){
    let buttonCancel = document.getElementById("buttonCancel");

    if(buttonCancel){
        buttonCancel.addEventListener('click', function(){
            window.location.href = "/";
        })
    }

})