#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - 6174
# Nome: Matheus Henrique Sobrinho
# RA: 245054
#####################################################

# Leitura do número N
def data_entrance():
    N = int(input())
    n = [int(k) for k in str(N)]
    return n

# Repetição do processo para geração de f(N) até obtermos o número 6174
def processing(argument, counter, saving):
    i = increasing_sequence(argument) # Transformando a lista em crescente
    d = decresing_sequence(argument) # Tranformando a lista em decrescente

    # Juntando os itens da lista e tranformando-os de volta em int
    C = int(''.join(i))
    D = int(''.join(d))

    # Tranformando argument em um numero inteiro
    sequence = []
    for item in argument:
        sequence.append(str(item))
    new_sequence = int(''.join(sequence))

    function = D - C # Funcao de Kaprekar
    if function != 6174:
        n = [int(k) for k in str(function)] # Tranformamos a function em uma lista novamente
        if counter <= 0 :
            data_saving(new_sequence)
            data_saving(function)
            counter +=1
            processing(n, counter, saving)
        else:
            data_saving(function)
            processing(n, counter, saving)
    else:
        if counter <= 0:
            data_saving(new_sequence)
            for item in saving:
                print(item)
        else:
            for item in saving:
                print(item)
        print(function)

def increasing_sequence(number):
    new_sequence = sorted(number)
    new_list = []
    for item in new_sequence:
        new_list.append(str(item))
    return new_list

def decresing_sequence(number):
    new_sequence = sorted(number, reverse=True)
    new_list = []
    for item in new_sequence:
        new_list.append(str(item))
    return new_list

def data_saving(argument):
    saving.append(argument)

if __name__ == "__main__":
    USER_DATA = data_entrance()
    saving = []
    counter = 0
    processing(USER_DATA, counter, saving)