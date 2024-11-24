###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Conjectura de Collatz
# Nome: Matheus Henrique Sobrinho
# RA: 245054
###################################################

# Inicialização das variáveis

n_var = int(input())
qntd_numeros = []

for number in range(n_var):
    numeros = int(input())
    qntd_numeros.append(numeros)

repeticoes = 0

# Leitura da sequência de números

while repeticoes < len(qntd_numeros):
    n = qntd_numeros[repeticoes]
    a = int(n)

    lista_par = []
    lista_impar = []

    while (a != 1):
        if (a % 2 == 0):
            lista_par.append(a)
            a /= 2
        else:
            lista_impar.append(a)
            a = (3*a)+1

    lista_impar.append(a)

    #contando itens das listas

    contador_par = len(lista_par)
    contador_impar = len(lista_impar)

    #Ordenando e concatenando as listas de par e impar

    lista1 = lista_par + lista_impar
    lista_completa = sorted(lista1)
    maior_valor = lista_completa[-1]

    # Impressão das informações de saída

    print("Valor inicial:", n)
    print("Numeros Pares:",  contador_par)
    print("Numeros Impares:", contador_impar )
    print("Maior Numero:", int(maior_valor) )

    repeticoes += 1