import PySimpleGUI as sg
from random import randint

senha = randint(1000, 9999)
tentativas = 0
game_win = False

def verificar_distancia(input):
    global game_win # usado para dizer que é uma variavél global, e nao apenas da def
    distancia = senha - input

    if distancia == 0:
        texto_distancia = "Acertou!"
        game_win = True
    elif abs(distancia) >= 3000:
        texto_distancia = "Está a mais de 3000 de distância"
    elif abs(distancia) >= 2000:
        texto_distancia = "Está entre 2000 - 3000 de distância"
    elif abs(distancia) >= 1000:
        texto_distancia = "Está entre 1000 - 2000 de distância"
    elif abs(distancia) >= 500:
        texto_distancia = "Está entre 500 - 1000 de distância"
    elif abs(distancia) >= 400:
        texto_distancia = "Está entre 400 - 500 de distância"
    elif abs(distancia) >= 300:
        texto_distancia = "Está entre 300 - 400 de distância"
    elif abs(distancia) >= 200:
        texto_distancia = "Está entre 200 - 300 de distância"
    elif abs(distancia) >= 100:
        texto_distancia = "Está entre 100 - 200 de distância"
    elif abs(distancia) >= 50:
        texto_distancia = "Está entre 50 - 100 de distância"
    elif abs(distancia) >= 40:
        texto_distancia = "Está entre 40 - 50 de distância"
    elif abs(distancia) >= 30:
        texto_distancia = "Está entre 30 - 40 de distância"
    elif abs(distancia) >= 20:
        texto_distancia = "Está entre 20 - 30 de distância"
    elif abs(distancia) >= 10:
        texto_distancia = "Está entre 10 - 20 de distância"
    elif abs(distancia) >= 5:
        texto_distancia = "Está entre 5 - 10 de distância"
    elif abs(distancia) == 4:
        texto_distancia = "Está a 4 de distância"
    elif abs(distancia) == 3:
        texto_distancia = "Está a 3 de distância"
    elif abs(distancia) == 2:
        texto_distancia = "Está a 2 de distância"
    elif abs(distancia) == 1:
        texto_distancia = "Está a apenas 1 de distância"

    print(f'ditância: {distancia}')
    print(texto_distancia)
    return texto_distancia # para ser usado fora da def
def sistema_potuação(tentativas):
    pontuacao = 10100 - (tentativas * 100) #diminui 100 pontos a cada tentativa
    return pontuacao


# layout da interface
layout = [
    # texto informativo
    [sg.Text("Irá ser gerada uma senha de 4 digitos, será que consegue acertar com poucas dicas?")],

    # mostra senha para testes
    [sg.Button("Mostrar Senha"), sg.Button("Ocultar Senha"),sg.Text("", key="-mostrar_senha-")],

    # recebe tentativa do usuário / botão de enviar
    [sg.Input(key="-tentativa-"), sg.Button("Enviar")],

    # mostra o status do jogo
    [sg.Text("", key="-texto_de_status-")],
    [sg.Text("", key="-pontuacao-"), sg.Text("", key="-tentativas-")]
]


# Interface
window = sg.Window('Jogo da Senha', layout)

while True:
    events, value = window.read()

    # fechar programa quando "X" é precionado
    if events == sg.WIN_CLOSED:
        break
    
    # mostra a senha se o botão for apertado
    if events == "Mostrar Senha":
        window["-mostrar_senha-"].update(f"Senha: {senha}")
    if events == "Ocultar Senha":
        window["-mostrar_senha-"].update("")
    
    if events == "Enviar":
        tentativas += 1
        window["-tentativas-"].update(f"tentativas: {tentativas}")
        try:
            # recebe o valor digitado pelo usuário
            input_num = int(value["-tentativa-"])
            texto_distancia = verificar_distancia(input_num)
            window["-texto_de_status-"].update(texto_distancia)

            # atualiza a pontuação e exibe
            pontuacao = sistema_potuação(tentativas)
            window["-pontuacao-"].update(f"pontuação: {pontuacao}")

        # se o usuário não digitar um numero inteiro
        except ValueError:
            sg.popup("Por favor, digite um numero inteiro válido")

        # verifica se ganhou o jogo
        if game_win:
            sg.popup("Novo Jogo?")
            senha = randint(1000, 9999)
            tentativas = 0
            game_win = False
            window["-mostrar_senha-"].update("")
        
window.close()