document.addEventListener("DOMContentLoaded", function(){
    let newEventos = document.getElementById('button-new-evento');

    if(newEventos){
        newEventos.addEventListener('click', function(){
            window.location.href = 'eventos'
        })
    }

})