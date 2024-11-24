# Primeiro receberemos um tabuleiro 10x10 onde "X" significa que existe uma mina que explodirá caso pise nela
# Também existirá um ponto "+" que é o local onde se deve chegar
# A posicao inicial será ditada por outra entrada no programa, onde A até J significaram as linhas e números de 1 a 10 serão as colunas
# O objetivo do programa é receber este campo e calcular o caminho mais rápido até este ponto de saída.
# Testaremos todos os tipos de movimentação tanto para os lados quanto para diagonais

# ENTRADA
def board_entries():
    board = [] # Tabuleiro do campo minado inserido pelo usuário
    for _ in range(10):
        board.append(input().split())
    
    start_location = input().split() # Localizacao de partida
    safe_location = input().split() # Localizacao que devemos cehgar

    return board, start_location, safe_location
    

def catching_mines(board):
    mine_index = {}
    line = 0
    for k in board:
        if k == board[line]:
            index_line = line
            line += 1
        else:
            print("ERROR 1")
            break
        for i in range(len(k)):
            if k[i] == "x":
                if k[i] not in mine_index:
                    itens_add = []
                    itens_add.append([index_line, i])
                    mine_index[k[i]] = itens_add
                else:
                    itens_add = []
                    for _ in mine_index[k[i]]:
                        itens_add.append(_)
                    itens_add.append([index_line, i])
                    mine_index[k[i]] = itens_add
    
    return mine_index

def walking_carefully(mines, board, start, end):
    letter = "ABCDEFGHIJ"
    start[0] = letter.find(start[0])
    start[1] = int(start[1]) - 1

    board[start[0]][start[1]] = "+"
    

if __name__ == "__main__":
    board, start, safe = board_entries()
    mine_index = catching_mines(board)
    walking_carefully(mine_index, board, start, safe)