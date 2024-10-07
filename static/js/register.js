const fomrRegister = {
    nome: ()=> document.getElementById('username'),
    email: ()=> document.getElementById('email'),
    senha1: ()=> document.getElementById('password'),
    senha2:()=> document.getElementById('password2'),

    buttonRegister: ()=> document.getElementById('buttonRegister'),
    buttonLogin: () => document.getElementById('buttonLogin')

}

function validarForms(){
    if(fomrRegister.nome() && fomrRegister.email() && fomrRegister.senha1() && fomrRegister.senha2()){
        if(fomrRegister.senha1().value == fomrRegister.senha2().value && fomrRegister.senha1().value != ""){
            return fomrRegister.buttonRegister().classList.remove('disabled_button')    
        }else{
            return fomrRegister.buttonRegister().classList.add('disabled_button')
        }
    }
}

function validarLogin(){

    if(fomrRegister.senha1().value && fomrRegister.nome().value){
        return fomrRegister.buttonLogin().classList.remove('disabled_button') 
    }
    return fomrRegister.buttonLogin().classList.add('disabled_button') 
}