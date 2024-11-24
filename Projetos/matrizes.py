'''
matriz = [[0 for _ in range(3)] for _ in range(3)]

matriz_range = len(matriz) 

for l in range(matriz_range):
    for c in range(matriz_range):
        matriz[l][c] = int(input())
        matriz[l][c] = str(matriz[l][c])

for l in matriz:
    print(" ".join(l))
'''

lst = [1, 2, 3, 4, 5, 4, 1, 4, 2, 1, 3, 5, 5, 1, 0, 1, 4, 2, 5, 5, 4, 3, 2, 1, 0, 0, 0]

lst = list(reversed(lst))

print(lst)