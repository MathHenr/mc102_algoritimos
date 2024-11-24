#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Aventura na Amazônia
# Nome: Matheus Henrique Sobrinho
# RA: 245054
#####################################################

# Lendo as entradas
def leitura_entrada():
    board = [] # Pegando tabuleiro e traformando em uma matriz com listas
    for _ in range(10):
        board.append(input().split())

    number_guess = int(input())
    guess = [] # Pegando os palpites e colocando-os em um lista para checar mais para frente do código
    for _ in range(number_guess):
        guess.append(input().split())
    return board, guess

# Processando os valores de entrada
def testing_guesses(board, guesses, ships):
    letters_list = "ABCDEFGHIJ"
    name_ships = [] # Pegando todos os navios que existem
    for keys in ships:
        name_ships.append(keys)

    for _ in range(len(guesses)):
        var = guesses[_]
        var[0] = letters_list.find(var[0]) # Mudando letras para números inteiros
        var[1] = int(var[1]) - 1 # Transformando os números em valores inteiros e não em strings. E tirando - 1 para pegar posicoes(index) em board
        if board[var[0]][var[1]] != ".":
            ship = board[var[0]][var[1]]
            if ship in ships:
                for k in ships[ship]:
                    if var == k:
                        ships[ship].remove(k)
                if not ships[ship] == []:
                    print(f"atingiu o navio {ship}")
                else:
                    print(f"afundou o navio {ship}")
        else:
            print("agua")


# Lendo as posicoes dos navios para ver se afundou ou não
def reading_board(board):
    counter = 0
    ship_index = {}
    for k in board:
        while counter in range(len(board)):
            if k == board[counter]:
                index_k = counter
                counter += 1
                break
            counter += 1
        for _ in range(len(k)):
            if k[_] != ".":
                ship = k[_]
                if ship not in ship_index:
                    counter_index = []
                    counter_index.append([index_k, _])
                    ship_index[ship] = counter_index
                else:
                    counter_index = []
                    if ship in ship_index:
                        for a in ship_index[ship]:
                            counter_index.append(a)
                    counter_index.append([index_k, _])
                ship_index[ship] = counter_index
    return ship_index

if __name__ == "__main__":
    board, guess = leitura_entrada()
    dict_ships = reading_board(board)
    testing_guesses(board, guess, dict_ships)