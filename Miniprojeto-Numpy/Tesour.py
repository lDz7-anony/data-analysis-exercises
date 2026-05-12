import numpy as np
from time import sleep
from colorama import init, Fore



def print_inicio():
    print("=-="*10)
    print("Bem-vindo ao jogo do tesouro!")
    print("=-="*10)
    sleep(2)
    for i in range(5):
        print("*"*i)
    for i in range(5):
        print("*"*(5-i))




def selecao_dificuldade():
    print("Selecione a Dificuldade")
    dificuldade = input("1 - Fácil, 2 - Médio, 3 - Difícil: ")
    #verificação da dificuldade, caso o usuário digite algo diferente de 1,2 ou 3, ele irá pedir para digitar novamente
    while(dificuldade not in ['1','2','3']):
        print("Dificuldade inválida, tente novamente.")
        dificuldade = input("1 - Fácil, 2 - Médio, 3 - Difícil: ")
    return dificuldade




def gera_mapa(dificuldade):
        
    if(dificuldade == '1'):
        size=5
        print("Dificuldade Fácil selecionada.")
        print(f"O tesouro está escondido em um mapa {size}x{size}.")
    elif(dificuldade == '2'):
        size=10
        print("Dificuldade Médio selecionada.")
        print(f"O tesouro está escondido em um mapa {size}x{size}.")
    else:
        size=15
        print("Dificuldade Difícil selecionada.")
        print(f"O tesouro está escondido em um mapa {size}x{size}.")
        #criando o mapa, onde o tesouro estará escondido, o número 99 representa o tesouro, os outros números são apenas para preencher o mapa
    mapa = np.random.randint(1,10,size = (size,size))
    mapa[np.random.randint(1,size), np.random.randint(0,size)] = 99
    mapa_visivel = np.zeros((size,size), dtype=int)
    tentativas = size*size
    return mapa, mapa_visivel, tentativas




def andar(tecla, linha, coluna, mapa):
    if(tecla == 'A' and coluna > 0):
        coluna-=1
    elif(tecla == 'D' and coluna < mapa.shape[1]-1):
        coluna+=1
    elif(tecla == 'W' and linha > 0):
        linha-=1
    elif(tecla == 'S' and linha < mapa.shape[0]-1):
        linha+=1
    return linha, coluna




def pega_tecla():
    tecla = input("Hora de andar:").upper()
    while(tecla not in ['A','S','D','W']):
        print("Tecla inválida, tente novamente.")
        tecla = input("Hora de andar:").upper()
    return tecla




def acertou(linha, coluna, mapa):
    print("=-"*10)
    mapa_visivel[linha, coluna] = mapa[linha, coluna]
    for i in range(mapa.shape[1]):
        for j in range(mapa.shape[0]):
            if(mapa_visivel[i,j] == mapa[linha,coluna]):
                print(Fore.GREEN + f"{mapa_visivel[linha,coluna]}", end=" ")
            else:
                print(Fore.WHITE + f"{mapa_visivel[i,j]}", end=" ")
        print()
    print("=-"*10)
    print("Parabéns, você encontrou o tesouro!")
    print(f"Pontuação: {tentativas}")




def errou(linha, coluna, mapa):
    mapa_visivel[linha, coluna] = mapa[linha, coluna]
    print("."*10)
    for i in range(mapa.shape[1]):
        for j in range(mapa.shape[0]):
            if(mapa_visivel[i,j] != 0):
                print(Fore.RED + f"{mapa_visivel[linha,coluna]}", end=" ")
            else:
                print(Fore.WHITE + f"{mapa_visivel[i,j]}", end=" ")
        print()
    print("."*10)











if(__name__ == "__main__"):
    linha=coluna=0
    init()#ativar colorama  
    print_inicio()
    dificuldade = selecao_dificuldade()
    mapa, mapa_visivel, tentativas = gera_mapa(dificuldade)
#enquanto nao acertar o jogo não para, para sair CTRL+C
    while(True):
        tentativas-=1

        tecla = pega_tecla()
        linha, coluna = andar(tecla, linha, coluna, mapa)

        
        if(mapa[linha,coluna] == 99):
            acertou(linha, coluna, mapa)
            break
        else:
            errou(linha, coluna, mapa)
            

        