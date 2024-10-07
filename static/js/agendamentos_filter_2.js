document.addEventListener("DOMContentLoaded", function(){

    var filters = document.querySelectorAll('.filter-2');

    filters.forEach(function(filter){

        filter.addEventListener("click", function(){
            let tip = filter.innerHTML;

            console.log(tip)

            let allId = document.getElementById('all')
            let inId = document.getElementById('in')
            let out = document.getElementById('out');

            let all = document.getElementById('evento_all')
            let timeIn =  document.getElementById('evento_in')
            let timeOut =  document.getElementById('evento_out')



            if(tip.includes("All")){
                allId.classList.add('select')
                inId.classList.remove('select')
                out.classList.remove('select')

                if(all){ all.classList.remove('no_select')}
                if(timeIn){ timeIn.classList.add('no_select') }
                if(timeOut){   timeOut.classList.add('no_select')}

            
            }else if(tip.includes("Time-in")){
                allId.classList.remove('select')
                inId.classList.add('select')
                out.classList.remove('select')


                if(timeIn){timeIn.classList.remove('no_select') }            
                if(all){all.classList.add('no_select')}
                if(timeOut){ timeOut.classList.add('no_select')}

            }else{
                allId.classList.remove('select')
                inId.classList.remove('select')
                out.classList.add('select')

                if(timeOut){ timeOut.classList.remove('no_select')}
                if(all){  all.classList.add('no_select')}
                if(timeIn){  timeIn.classList.add('no_select')}

            
            }
        }
        )})

});    