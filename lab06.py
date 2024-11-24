###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Eleição 2022
# Nome: Matheus Henrique Sobrinho  
# RA: 245054
###################################################

# Leitura no número de candidatos

n_candidatos = int(input())

# Leitura do nome dos candidatos
candidatos = []

for pessoas in range(n_candidatos):
    nome_candidato = str(input())
    candidatos.append(nome_candidato)

# Leitura dos votos
votos_compr = n_candidatos + 2
votos = []

for number in range(votos_compr):
    votacao = int(input())
    votos.append(votacao)

total_votos = sum(votos)

#ANALISE DOS VOTOS E CANDIDATOS!!!!

#verificando votos Total, Brancos e Nulos
votos_nulos = votos[votos_compr - 1]
votos_brancos = votos[votos_compr - 2]
del(votos[votos_compr - 1])
del(votos[votos_compr - 2])

total_votos_validos = sum(votos)

#Verficando se precisa de 2 turno
metade_votos = total_votos_validos / 2
maior_votado = max(votos)
indice_primeiro_votado = votos.index(maior_votado)
nome_maior_votado = candidatos[indice_primeiro_votado]

if maior_votado > metade_votos:
    eleito = candidatos[indice_primeiro_votado]
    print(f"{eleito} foi o vencedor da eleição")
    print(f"Total de votos: {total_votos}")
    print(f"Votos válidos: {total_votos_validos}")
else:
    del(votos[indice_primeiro_votado])
    del(candidatos[indice_primeiro_votado])
    segundo_votado = max(votos)
    indice_segundo_votado = votos.index(segundo_votado) + 1
    #Pegando o segundo candidato para 2 turno
    
    candidatos.insert(indice_primeiro_votado, nome_maior_votado)

    primeiro_votado = candidatos[indice_primeiro_votado]
    segundo_votado = candidatos[indice_segundo_votado]
    print("Haverá segundo turno entre:")
    print(primeiro_votado)
    print(segundo_votado)
    print(f"Total de votos: {total_votos}")
    print(f"Votos válidos: {total_votos_validos}")

