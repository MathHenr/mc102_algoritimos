###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Ballon d'Or
# Nome: Matheus Henrique Sobrinho
# RA: 245054
###################################################

#Importando defaultdict para pegar indice dos jogadores repetidos e não repetidos
from collections import defaultdict

# Leitura de dados

def main():

    jurados = int(input())

# Processamento

    indicados = jogadores_indicados(jurados)

# Pegar Nomer e associar os pontos
    resultados, nomes, tamanho = contagem_de_votos(indicados)

# Impressão da saída
    i = 0

    while i < tamanho:
        #Pegando maior nota da lista
        nota_maxima = max(resultados)
        index_nota_max = resultados.index(nota_maxima)

        #Pegando nome do jogador com a maior nota
        jogador_nota_max = nomes[index_nota_max]
        
        print(f"{jogador_nota_max}:", nota_maxima)

        #Excluindo nota e jogador para pegar proxima nota maior e jogador
        del(resultados[index_nota_max])
        del(nomes[index_nota_max])
        i+=1

def contagem_de_votos(indicados):
    lista = []
    lista_nome = []

    chaves = defaultdict(list)
    print(indicados)
    for a in indicados:
        for chave, value in enumerate(a):
            chaves[value].append(chave)

    print(chaves)


    for value in chaves:
        lista_nome.append(value)
        x = chaves[value]
        if len(x) != 0:
            soma_pontos = []
            for a in x:
                value = switcher(a)
                soma_pontos.append(value)
            soma_pontos = sum(soma_pontos)
            lista.extend([soma_pontos])

    return lista, lista_nome, len(lista)



def switcher(argument):
    if argument == 0:
        return 6
    else:
        if argument == 1:
            return 4
        else:
            if argument == 2:
                return 3
            else:
                if argument == 3:
                    return 2
                else:
                    return 1



def jogadores_indicados(number):
    indicados = []

    for _ in range(number):
        jogadores =[]
        J1 = str(input())
        jogadores.append(J1)
        J2 = str(input())
        jogadores.append(J2)
        J3 = str(input())
        jogadores.append(J3)
        J4 = str(input())
        jogadores.append(J4)
        J5 = str(input())
        jogadores.append(J5)

        indicados.append(jogadores)

    return indicados



main()