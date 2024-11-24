matriz_susy = []
minha_matriz = []

for k in range(20):
    M1 = input().split()
    minha_matriz.append(M1)

for k in range(20):
    M1 = input().split()
    matriz_susy.append(M1)
i = True

for k in range(len(matriz_susy)):
    if matriz_susy[k] != minha_matriz[k]:
        print(f"Existe um erro na linha {k + 1}")
        i = False

if i != False:
    print("Sao iguais")