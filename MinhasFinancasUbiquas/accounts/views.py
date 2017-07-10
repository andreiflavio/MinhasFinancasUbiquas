from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login # funcao que salva o usuario na sessao

# Create your views here.
def home(request):    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            #agora, basta logar o usuario e ser feliz.
            login(request, form.get_user())
            return HttpResponseRedirect("/") # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "login.html", {"form_login": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "login.html", {"form_login": AuthenticationForm()})

def register(request):
    pass

def password_reset(request):
    pass
