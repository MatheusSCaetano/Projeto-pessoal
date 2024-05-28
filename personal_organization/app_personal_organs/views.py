from django.shortcuts import render
from .models import Usuario
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView): #criar uma url que chame essa view
     template_name = 'tela_cadastro.html'        

def usuarios (request): #pegando os gets da tela
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.email = request.get('email')
        novo_usuario.email2 = request.get('confirmar_email')
        if novo_usuario.email == novo_usuario.email2:
            novo_usuario.senha = request.POST.get('senha')
            novo_usuario.senha2 = request.POST.get('confirmar_senha')
            if novo_usuario.senha == novo_usuario.senha2:
                novo_usuario.save()
            else: # else da senha invalida
                return render(request, 'interface_grafica/cadastro.html'),{'mensagem':'As senhas devvem ser identicas'}
        else:
                return render(request, 'interface_grafica/cadastro.html'),{'mensagem': 'Os dois e-mail são diferentes'}    
    else:
         return render(request,'interface_grafica/tela_login.html')




