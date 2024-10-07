document.addEventListener("DOMContentLoaded", function(){
        
    let footer = document.querySelector(".footer");

    function checkMeidaQuery(){

        if(window.matchMedia('(max-width: 420px').matches) {
            footer.classList.remove("footer")
        }
        else{
            footer.classList.add("footer")
        }
    }
    checkMeidaQuery()
    window.addEventListener('resize', checkMeidaQuery)
})