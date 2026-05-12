import numpy as np


def colocar_peca(tabuleiro, linha, coluna, peca):
    if(tabuleiro[linha, coluna] == 0):
        tabuleiro[linha, coluna] = peca
        return True
    return False    

def verifica_vitoria(tabuleiro, peca):
    
    linhas = np.any(np.all(tabuleiro == peca, axis=1))#verifica se todas as colunas de uma linha sao iguais a peca
    colunas = np.any(np.all(tabuleiro == peca, axis=0))#verifica se todas as linhas de uma coluna sao iguais a peca
    diagonais = np.any(np.all(np.diag(tabuleiro) == peca)) or np.any(np.all(np.diag(np.fliplr(tabuleiro)) == peca)) #verifica se todas as posicoes da diagonal principal ou secundaria sao iguais a peca
    
    return any([linhas, colunas, diagonais])


def jogar():
    tabuleiro = np.zeros((3,3), dtype=int)
    jogador_atual = 1
    
    vencedor = False
    empate = False

    while not vencedor and not empate:
        print(tabuleiro)
        linha = int(input(f"Jogador, digite a linha (0, 1 ou 2): "))
        coluna = int(input(f"Jogador, digite a coluna (0, 1 ou 2): "))
        
        colocar_peca(tabuleiro, linha, coluna, jogador_atual)
        
        if verifica_vitoria(tabuleiro, jogador_atual):
            vencedor = True
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
        elif np.all(tabuleiro != 0):
            empate = True
            print("Empate! O tabuleiro está cheio.")
        else:
            jogador_atual = 2 if jogador_atual == 1 else 1

        
    print(tabuleiro)
    if( vencedor):
        print(f"Parabéns! Jogador {jogador_atual} venceu!")
    elif( empate):
        print("Empate! O tabuleiro está cheio.")
    else:
        print("O jogo terminou sem um vencedor ou empate.")


jogar()