###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Noite de Sono
# Nome: Matheus Henrique Sobrinho
# RA: 245054
###################################################

# Leitura de dados

horaDeitou = int(input())  #Hora que dormiu
minutoDeitou = int(input())  #Minuto que dormiu
horaAcordou = int(input())  #Hora que acordou
minutoAcordou = int(input())  #Minuto que acordou

# Cálculo do tempo dormido

minutoDormiu = minutoDeitou/60  
horaDormida = horaDeitou + minutoDormiu   #Transformando Hora que dormiu em numero inteiro para calcular com hora que acordou

minutoAcordado = minutoAcordou/60
horaAcordada = horaAcordou + minutoAcordado  #Realizando a mesma conversão para numero inteiro

#A conversão se deve para quando os minutos interferirem com a contagem de horas, ex 22h45 até 06h15 - tranfosmando-as em 22,75 e 06,25
#para que soma seja realizada de forma correta!!

horaCalculada = (24 - horaDormida) + horaAcordada

# Impressão da resposta

if horaCalculada >= 8:
    print("True")
else:
    print("False")