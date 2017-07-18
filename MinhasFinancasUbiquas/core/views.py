from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def cadPessoa(request):    
    return render(request, 'core/pessoa.html')
