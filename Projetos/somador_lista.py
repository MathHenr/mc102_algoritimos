def contador(numero, lista):
    number = lista[numero]
    if numero < 0:
        return 1

    return number / contador(numero - 1, lista)

if __name__ == "__main__":
    n = int(input())
    lista = []

    for k in range(n):
        n1 = int(input())
        lista.append(n1)

    x = contador(n - 1, lista)

    print(int(x), lista)