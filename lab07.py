
###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Encaixe Perfeito
# Nome: Matheus Henrique Sobrinho  
# RA: 245054
###################################################

#Recebendo valores de INPUT

number = int(input())
lista = []

for _ in range (number):
    P1 = [int(n) for n in input().split()]
    P2 = [int(n) for n in input().split()]

    lista.append(P1)
    lista.append(P2)

repeticao = 0

while repeticao < len(lista) - 1:
    #Pegando peças
    peca1 = lista[repeticao]
    peca2 = lista[repeticao + 1]

    #Listas de pontos
    pontos = []

    #Variavei de controle de indice das posicoes das pecas
    i = 0
    j = 0 
    
    while i < len(peca2):
        #Lista de encaixes
        encaixe = []
        pontuacao = []

        #Atribuindo caracteristica "Normal" a peça 1
        status_peca1 = "Normal"

        #verificando encaixe perfeito
        z = i

        while j < len(peca1):
            if len(peca1) + i <= len(peca2):
                if z < len(peca2):
                    encaixe_peca1 = peca1[j]
                    encaixe_peca2 = peca2[z]
                    soma = encaixe_peca1 + encaixe_peca2
                    encaixe.append(soma)
                    j+=1
                    z+=1
            else:
                break
        
        if len(encaixe) != 0:
            soma_max = max(encaixe)

            for n in encaixe:
                n_pontos = soma_max - n
                pontuacao.append(n_pontos)
                
            pontuacao = sum(pontuacao)
            pontos.append(pontuacao)
            j = 0
            i+=1
        else:
            #Pegando menor valor de pontos
            valor = min(pontos)

            if valor == 0:
                print("Encaixe Perfeito!")
                print("Posicao de Encaixe:", pontos.index(valor) + 1)
                print("Peca 1:", status_peca1)
                break
            else:
                peca1 = list(reversed(peca1))

                #Pontos Peça invertida
                pontos_invertida = []

                #Variavei de controle de indice das posicoes das pecas
                a = 0
                b = 0

                while a < len(peca2) * 2:
                    #Lista de encaixes
                    encaixe = []
                    pontuacao = []

                    #verificando encaixe perfeito
                    z = a

                    while b < len(peca1):
                        if len(peca1) + a <= len(peca2):
                            if z < len(peca2):
                                encaixe_peca1 = peca1[b]
                                encaixe_peca2 = peca2[z]
                                soma = encaixe_peca1 + encaixe_peca2
                                encaixe.append(soma)
                                b+=1
                                z+=1
                        else:
                            break
                    if len(encaixe) != 0:
                        soma_max = max(encaixe)

                        for n in encaixe:
                            n_pontos = soma_max - n
                            pontuacao.append(n_pontos)
                            
                        pontuacao = sum(pontuacao)
                        pontos_invertida.append(pontuacao)
                        b = 0
                        a+=1
                    else:
                        #Pegando menor valor de pontos
                        valor_normal = min(pontos)
                        valor_invertido = min(pontos_invertida)

                        if valor_invertido < valor_normal:
                            status_peca1 = "Invertida"
                            if valor_invertido == 0:
                                print("Encaixe Perfeito!")
                                print("Posicao de Encaixe:", pontos_invertida.index(valor_invertido) + 1)
                                print("Peca 1:", status_peca1)
                                break
                            else:
                                #Pegando posicao de menor valor
                                indice_valor = pontos_invertida.index(valor_invertido)

                                print("Pontuacao:", valor_invertido)
                                print("Posicao de Encaixe:", indice_valor + 1)
                                print("Peca 1:", status_peca1)
                                break
                        else:
                            if valor_normal == 0:
                                print("Encaixe Perfeito!")
                                print("Posicao de Encaixe:", pontos.index(valor_normal) + 1)
                                print("Peca 1:", status_peca1)
                                break
                            else:
                                #Pegando posicao de menor valor
                                indice_valor = pontos.index(valor_normal)

                                print("Pontuacao:", valor_normal)
                                print("Posicao de Encaixe:", indice_valor + 1)
                                print("Peca 1:", status_peca1)
                                break
                break

    repeticao+=2

    

