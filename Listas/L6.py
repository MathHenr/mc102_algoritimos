# 3
'''
def f_calcula(numero):
    if numero == 0:
        return 0
    else:
        if numero > 0:
            return numero + f_calcula(numero - 1)

if __name__ == "__main__":
    number = int(input())
    number_test = f_calcula(number)

    print(number_test)
'''
'''
x = "meu nome"

if x != int():
    print(x)
else:
    print("Nao é uma string!!")
'''
'''
lista = ['A', [2, 2], 'A', [2, 3], 'A', [2, 4], 'C', [4, 7], 'C', [4, 8], 'C', [4, 9], 'B', [6, 4], 'B', [7, 4]]

a = "A"
coordenadas = [0, 2]

if a not in lista:
    print('nao ta na lista')
else:
    if a in lista and coordenadas in lista:
        print('ok')
    else:
        print('nao ta na lista - 2')
'''
lista = [{'Michael Owen': [[0, 0], [1, 0]], 'Raul': [1, 3, 4, 2, 1], 'Oliver Kahn': [2, 2, 3, 4, 2], 'Luis Figo': [3], 'Zinedine Zidane': [4, 1], 'Francesco Totti': [1, 2, 3, 3], 'Rivaldo': [4], 'Andriy Shevchenko': [0, 4], 'Thierry Henry': [0]}]


print(type(lista))