###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Detector de Palíndromos
# Nome: Matheus Henrique Sobrinho
# RA: 245054
###################################################
def main():
    number = int(input())

    escrita = []
    palavras_pali = []
    repeticao = set()

    for x in range(number):
        frase =  str(input())
        frase_nova = frase.replace(",","")
        frase_nova = frase_nova.replace(".","")
        frase_nova = frase_nova.replace("!","")
        frase_nova = frase_nova.replace("?","")
        frase_nova = frase_nova.replace(":","")
        frase_nova = frase_nova.lower()
        frase_nova = frase_nova.split()
        escrita.append(frase_nova)

    palindromos = leitura_das_frases(escrita)
    
    for n in palindromos:
        if n not in palavras_pali:
            palavras_pali.append(n)
        else:
            repeticao.add(n)
    
    n_rep = numero_de_repeticoes(repeticao, palindromos)

    if len(palindromos) != 0:
        for a in palavras_pali:
            if a not in n_rep:
                print(a ,"1")
            else:
                n = n_rep.index(a)
                n+=1
                n = n_rep[n]
                print(a,n)

def numero_de_repeticoes(number, lista):
    n_repeticao = []
    for a in number:
        rep = lista.count(a)
        if rep != 0:
            n_repeticao.append(a)
            n_repeticao.append(rep)
    return n_repeticao

def leitura_das_frases(frases):
    lista_palindromo = []
    leitura = 0

    while leitura < len(frases):
        item = frases[leitura]

        i = 0   
        j = len(item) - 1

        while i <= j:
            palavra = item[i]
            if palavra == palavra[::-1]:
                lista_palindromo.append(palavra)
                i+=1
            else:
                i+=1
        leitura+=1

    return lista_palindromo

main()