###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Batalha na Ponte de Piltover
# Nome: Matheus Henrique Sobrinho
# RA: 245054
###################################################

# !!!!!!! Se a vida de quem ataca for menor de quem recebe o dano, o dano cai pela metade

# Leitura da vida de Jinx e Ekko


hp_jinx = int(input())
hp_ekko = int(input())

# Leitura dos ataques da Jinx

#Numeros de ataque e danos da Jinx

n_atq_jinx = int(input())
dano_jinx = []

for number in range(n_atq_jinx):
    dano_j = int(input())
    dano_jinx.append(dano_j)

# Leitura dos ataques do Ekko

#Numeros de ataque e danos da Ekko

n_atq_ekko = int(input())
dano_ekko = []

for number in range(n_atq_ekko):
    dano_e = int(input())
    dano_ekko.append(dano_e)


#INICIO DA TRETA!!!

#Jinx batendo

jinx_bate = 0

while jinx_bate < len(dano_jinx):
    hit = dano_jinx[jinx_bate]
    if hp_jinx < hp_ekko:
        hit /= 2
        hp_ekko -= hit
        if  hp_ekko < 0:
            hp_ekko = 0
            break
        else:
            jinx_bate += 1
    else: 
        hp_ekko -= hit
        if  hp_ekko < 0:
            hp_ekko = 0
            break
        else:
            jinx_bate += 1

#Ekko batendo
if hp_ekko > 0:
    ekko_bate = 0

    while ekko_bate < len(dano_ekko):
        hit = dano_ekko[ekko_bate]
        if hp_ekko < hp_jinx:
            hit /= 2
            hp_jinx -= hit
            if hp_jinx < 0:
                hp_jinx = 0
                break
            else:
                ekko_bate += 1
        else:
            hp_jinx -= hit
            if hp_jinx < 0:
                hp_jinx = 0
                break
            else:
                ekko_bate += 1

#Analisar a vida dos 2 e ver o vencedor

if hp_ekko > hp_jinx:
    print('Vida da Jinx:', int(hp_jinx))
    print('Vida do Ekko:', int(hp_ekko))
    print('Ekko foi o vencedor da batalha')
else:
    if hp_ekko == hp_jinx:
        print('Vida da Jinx:', int(hp_jinx))
        print('Vida do Ekko:', int(hp_ekko))
        print('A batalha terminou empatada')
    else:
        print('Vida da Jinx:', int(hp_jinx))
        print('Vida do Ekko:', int(hp_ekko))
        print('Jinx foi a vencedora da batalha')

