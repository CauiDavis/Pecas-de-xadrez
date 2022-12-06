import numpy as np
import os
        
line = [2, 1, -1, -2, -2, -1, 1, 2]
column = [1, 2, 2, 1, -1, -2, -2, -1]

os.system('clear')
sizeboard = 8
lin = int(input('Digite a linha inicial do cavalo: '))
col = int(input('Digite a coluna inicial do cavalo: '))
board = np.zeros((sizeboard,sizeboard)) 
limit = sizeboard * sizeboard

def main(l, c): 

    board[l][c] = 1 

    movehorse(2, l, c) 

   
def movehorse(id, l, c): 
    if (id > limit ):
        print("solução encontrada")
        print(board)
        print("\n")
    k = 0 

    
    for k in range(8):
        x = l + line[k]
        y = c + column[k] 
        
        if(movacceptable(x, y)):
            board[x][y] = id
            movehorse(id + 1, x, y)
            board[x][y] = 0 
             
def movacceptable(x, y): 
    if((x >= 0 and x < sizeboard) and (y >= 0 and y < sizeboard) and (board[x][y] == 0)):
        return True
    else:
        return False

main(lin, col)