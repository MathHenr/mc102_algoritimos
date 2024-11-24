###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - BikeMax
# Nome: Matheus Henrique Sobrinho
# RA: 245054
###################################################

# Leitura de dados

sexo = str(input()) #Sexo deve ser somente M ou F
peso = int(input()) #Peso sendo sempre um valor inteiro
altura = int(input()) #Altura também sendo sempre um valor inteiro

# Seleção do modelo recomendado

if sexo == "M" or sexo == "m":
    if peso > 100:  #Modelo independente da altura do homem!
        print("CX-102")
    else:
        if altura <= 165:
            if peso <= 70:  #Modelos para peso menor que 70
                print("LX-39")
            else:  #Modelos para peso entre 70 e 100
                print("LX-40")
        else:
            if altura>165 and altura <= 190:
                if peso <= 80:  #Modelos para peso menor que 80 e alturas entre 165 e 190
                    print("BW-02")
                else:   #Modelos para peso maior que 80 e alturas entre 165 e 190
                    print("MM-107")
            else:  #Modelos para para altura maior que 190 independente do peso
                print("MM-107")

else:
    if sexo == "F" or sexo == "f":
        if altura <= 140: #Modelo independente do peso da mulher!
            print("LX-38") 
        else:
            if altura>140 and altura<=155: 
                if peso <= 90:  #Modelo para peso < 90
                    print("BW-03")
                else: #Modelos para peso acima de 90
                    print("CX-101")
            else:
                if altura>155 and altura<=170:
                    if peso <= 70:  #Modelos para peso menor ou igual a 70
                        print("BW-03")
                    else:  #Modelos para peso maior q 70
                        print("CX-101")
                else:
                    if altura > 170:
                        if peso <= 90:  #Modelos para peso menor ou igual a 90
                            print("BW-02")
                        else:
                            print("CX-102")