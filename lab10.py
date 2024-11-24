#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Aventura na Amazônia
# Nome: Matheus Henrique Sobrinho
# RA: 245054
#####################################################
def main():
    # Criação da matriz

    matriz = [['.'for _ in range(20)] for _ in range(20)]

    # Leitura da entrada e preenchimento da matriz

    linha, coluna = [int(n) for n in input().split()] # posição inicial

    # Lendo o trajeto realizado
    trajeto = trajeto_realizado()

    # Mudando valores recebidos em trajeto como str para int
    for l in range(len(trajeto)):
        if len(trajeto[l]) > 1:    
            trajeto[l][1] = int(trajeto[l][1])

    matriz = caminhada(matriz, linha, coluna, trajeto)

    # Imprimir valores (matriz) na tela
    for l in matriz:
        print(" ".join(l))

def trajeto_realizado():
    i = False
    trajeto = []

    while i != True:
        caminho = input().split()
        par_trajeto = []
        for k in range(len(caminho)):    
            if caminho[k] != "F":
                par_trajeto.append(caminho[k])
                i = False
            else:
                par_trajeto.append(caminho[k])
                i = True
        trajeto.append(par_trajeto)
    
    return trajeto

def caminhada(matriz, l, c, argument):
    p = l
    for k in range(len(matriz)):
        if k == p:
            matriz[l][c] = "+"
            coordenadas_A = []
            for x in range(len(argument)):
                if len(argument[x]) > 1:
                    direcao = argument[x][0]
                    # Fazer seguir as direcoes
                    casa = argument[x][1]
                    matriz, l, c = mapeamento(matriz, l, c, direcao, casa)
                else:
                    if argument[x][0] == "A":
                        matriz[l][c] = "#"
                        coordenadas_A.append([l,c]) # Temos o problema de que a trilha pode se sobrescrever alterando "#" para "+"
            matriz = marcador_de_arvores(matriz, coordenadas_A) # Pegando coordenadas onde tem arvores, para checar se esta marcado como "#"
    return matriz

def mapeamento(matriz, l, c, direcao, casas):
    if direcao == "S":
        for _ in range(casas):
            l+=1
            matriz[l][c] = "+"
    else:
        if direcao == "N":
            for _ in range(casas):
                l-=1
                matriz[l][c] = "+"
        else:
            if direcao == "O":
                for _ in range(casas):
                    c-=1
                    matriz[l][c] = "+"
            else:
                if direcao == "L":
                    for _ in range(casas):
                        c+=1
                        matriz[l][c] = "+"
    return matriz, l, c

def marcador_de_arvores(matriz, argument):
    for _ in argument:    
        l = _[0]
        c = _[1]
        matriz[l][c] = "#"
    return matriz
    
main()