from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User

from core.models import Evento
from datetime import datetime
# Create your views here.
@login_required(login_url='/login/')
def lista_eventos(request):
    """ """
    
    data_atual = datetime.now()
    usuario = request.user
    evento = Evento.objects
    dados = {}
    if request.GET.get('filter') == 'time-in':
        dados = {'filter': 'time-in',
                'eventos': evento.filter(usuario=usuario, data_evento__gt=data_atual)}
    elif request.GET.get('filter') == 'time-out':
        dados = {'filter': 'time-out',
                'eventos': evento.filter(usuario=usuario, data_evento__lt=data_atual)}
    else:
        dados = {'filter': 'all',
                'eventos': evento.filter(usuario=usuario)}
    
    return render(request, 'agendamentos.html', dados )    


@login_required(login_url='/login/')
def lista_eventos_2(request):
    data_atual = datetime.now()
    usuario = request.user
    evento = Evento.objects
    dados = {'evento_all': evento.filter(usuario=usuario),
            'evento_in':evento.filter(usuario=usuario, data_evento__gt=data_atual),
            'evento_out': evento.filter(usuario=usuario, data_evento__lt=data_atual)}

    return render(request, 'agendamentos_2.html', dados )  

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def register_user(request):
     
    return render(request, 'register.html')

def register_user_submit(request):

    if request.POST:

        email = request.POST.get('email')

        #messages.error(request, email_user)

        
        if  email !=  '':
            try:
                email_user = User.objects.get(email=email)
            except User.DoesNotExist:
                email_user = None

            if email_user is None:
                new_username = request.POST.get('new_username')
                if(new_username != ''):
                    new_password = request.POST.get('new_password')
                    new_password_2 = request.POST.get('new_password_2')
                    if(new_password == new_password_2 and (new_password != '' and new_password_2 !='')):

                        new_user = User.objects.create_user(username=new_username,
                                                            email=email, password=new_password,
                                                            is_staff=False, is_superuser=False)
                        #new_user.groups.add("visualizacao")
                        #messages.success(request, 'Usuário criado com sucesso.')
                        return redirect('/')
                    
                    elif not new_password and not new_password_2 :
                        messages.error(request, 'Senhas vazias')
                    else:
                        messages.error(request, 'As senhas não conferem')
                else:
                    messages.error(request, 'Nome de Usuario vazio')
            else:
                messages.error(request, 'E-mail já cadastrado')
        elif email == '':
            messages.error(request, 'Campo de email vazio')

    return redirect('/')





    #if request.method == 'POST':
       # form = UserForm(request.POST)
        #if form.is_valid():
         #   user = form.save(commit=False)
        #    user.set_password(form.cleaned_data['password'])
         #   user.save()
         #   messages.success(request, 'Usuário criado com sucesso.')
         #   return redirect('login')  # Redirecione para a página de login após o registro
   # else:
     #   form = UserForm()
  #  return render(request, 'register.html', {'form': form})


def login_user(request):
    return render(request, 'login.html')

def login_user_2(request):
    return render(request, 'login.html')

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return redirect('/')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def new_evento(request):

    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['eventos']= Evento.objects.get(id=id_evento)
    return render(request, 'eventos.html', dados)

@login_required(login_url='/login/')
def new_evento_submit(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        data_evento = request.POST.get('data_evento')
        usuario = request.user

        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.local = local
                evento.data_evento = data_evento
                evento.save()
        else:
            Evento.objects.create(titulo=titulo, 
                                descricao=descricao, 
                                local=local, 
                                data_evento=data_evento, 
                                usuario=usuario)
            
    return redirect('/')


def delete_evento(request, id_evento):


    usuario =request.user

    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        return render(request, '404.html')

    if usuario == evento.usuario:
        evento.delete()
        return redirect('/')
    else:
        return render(request, '404.html')