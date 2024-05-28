import PySimpleGUI as sg
import webbrowser


layout = [
    [sg.Text('Usuário')], #texto acima do input
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],
    [sg.Button('cadastre-se',key='link_cadastrese')],
]

janela = sg.Window('login',layout=layout) # definindo janela = através da variável "layout"

while True:
    event, values = janela.read() # event, values recebe os eventos que estao dentro da janela
    if event == sg.WIN_CLOSED: #se fechar -> dar um break no looping
        break
    elif event == 'login':
        senha_correta = '123' # pegar senha do bd
        usuario_correto = 'matheus' # pegar usuario do bd
        usuario = values['usuario']
        senha = values['senha']
        if usuario == usuario_correto and senha == senha_correta:
            janela['mensagem'].update('acesso permitido')
        else:
            janela['mensagem'].update('usuario ou senha incorreta')
    elif event == 'link_cadastrese':
        #obtendo o link do metadata diretamente
        link = 'interface_grafica/tela_cadastro.html' #variavel link recebendo o link
        webbrowser.open(link) #executanod o link em meu pacote webbrowser
