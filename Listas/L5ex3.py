def main():
    a = int(input("Digite um número a:"))
    b = int(input("Digite um número b:"))
    n = int(input("Digite um número n:"))
    funcao1 = teste(a,b,n)
    funcao2 = pitagorico(n, (b**2) + (a**2))
    print(f"Pelo teste temos que os parametros são: {funcao1}")
    print(f"Temos que a análise de N pitagorico foi que: {funcao2}")
    

def teste(a,b,n):
    if (a ** 2) + (b ** 2) == n:
        return True
    else:
        return False

def pitagorico(number, numberPita):
    if number == numberPita:
        return True
    else:
        return False

main()