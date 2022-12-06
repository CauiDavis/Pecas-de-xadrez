import numpy as np
import os
        
linha = [2, 1, -1, -2, -2, -1, 1, 2]
coluna = [1, 2, 2, 1, -1, -2, -2, -1]

os.system('clear')
tamanhoTab = 8
lin = int(input('Digite a linha inicial do cavalo: '))
col = int(input('Digite a coluna inicial do cavalo: '))
Tabuleiro = np.zeros((tamanhoTab,tamanhoTab)) 
limite = tamanhoTab * tamanhoTab

def principal(l, c): 

    Tabuleiro[l][c] = 1 

    correCavalinho(2, l, c) 

   
def correCavalinho(id, l, c): 
    if (id > limite ):
        print("solução encontrada")
        print(Tabuleiro)
        print("\n")
    k = 0 

    
    for k in range(8):
        x = l + linha[k]
        y = c + coluna[k] 
        
        if(movimentoAceitavel(x, y)):
            Tabuleiro[x][y] = id
            correCavalinho(id + 1, x, y)
            Tabuleiro[x][y] = 0 
             
def movimentoAceitavel(x, y): 
    if((x >= 0 and x < tamanhoTab) and (y >= 0 and y < tamanhoTab) and (Tabuleiro[x][y] == 0)):
        return True
    else:
        return False

principal(lin, col)