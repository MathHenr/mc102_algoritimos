###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Detector de Palíndromos
# Nome: Matheus Henrique Sobrinho
# RA: 245054
###################################################

# Leitura de dados

number = int(input())
escrita = []

for x in range(number):
    f = str(input())
    f = f.replace(",","")
    new_f = f.replace(".","")
    new_f = new_f.replace(":","")
    new_f = new_f.replace("!","")
    new_f = new_f.replace("?","")
    new_f = new_f.lower()
    new_f = new_f.split()
    escrita.append(new_f)

# Leitura das linhas do texto e tratamento
leitura = 0

#Utilizando o paramentro de que não ha nenhuma palavra que seja um palindromo
palindromo_lista = []

# Processamento

while leitura < len(escrita):
    #Pegando a frase da vez
    frase = escrita[leitura]

    #Variaveis para controle da lista "escrita"
    i = 0
    j = len(escrita[leitura]) - 1

    while i <= j:
        palavra_invertida = frase[i]
        palavra_invertida = palavra_invertida[::-1]
        if palavra_invertida != frase[i]:
            i+=1
        else:
            palindromo_lista.append(frase[i])
            i+=1
    leitura+=1

#Percorrendo a lista de palindromo
palindromos = []
repeticao = set()

for valor in palindromo_lista:
    if valor not in palindromos:
        palindromos.append(valor)
    else:
        repeticao.add(valor)

n_repeticao = []
print(palindromo_lista)

for a in repeticao:
    rep = palindromo_lista.count(a)
    if rep != 0:
        n_repeticao.append(a)
        n_repeticao.append(rep)

# Impressão da saída
if len(palindromo_lista) != 0:
    for _ in palindromos:
        if _ not in n_repeticao:
            print(_, "1")
        else:
            l = n_repeticao.index(_)
            l+=1
            l = n_repeticao[l]
            print(_,l)