###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Dia do Progresso I
# Nome: Matheus Henrique Sobrinho
# RA: 245054
###################################################
def data_entry(): # Pegando ponto de partida e mapa
    MAP = []
    LINES_MAP = int(input())
    for _ in range(LINES_MAP):
        MAP.append(input().split())

    START= [int(k) for k in input().split()]

    return MAP, START

def gatekeeper(Map):
    PATH = ["N","S","L","O"]
    portals = {}
    counter = 0 # Variavel para pegar indice de k!!

    for k in Map:
        while counter in range(len(Map)):
            if Map[counter] == k:
                index_line = counter
                counter +=1
                break
            else:
                counter+=1
        for _ in range(len(k)):
            if k[_] not in PATH and k[_] != "#" and k[_] != "*":
                portal_name = k[_]
                if portal_name not in portals:
                    location_portal = []
                    location_portal.append([index_line, _])
                    portals[portal_name] = location_portal
                else:
                    location_portal = []
                    for n in portals[portal_name]:
                        location_portal.append(n)
                    location_portal.append([index_line, _])
                portals[portal_name] = location_portal
    return portals

def testing_the_path(Map, local, counter):
    if counter < 200:
        counter +=1
        portals = gatekeeper(Map)
        path = "NSLO"
        position = Map[local[0]][local[1]]
        # Variavel para verificar se jayce passou dos limites do mapa ou se chegou em uma parede
        if position == "#":
            print("Jayce nao conseguiu chegar em Piltover")
            return
        if local[0] >= 0 and local[0] <= len(Map):
            key = True
        else:
            print("Jayce nao conseguiu chegar em Piltover")
            return
        if local[1] >= 0 and local[1] <= len(Map[0]):
            key = True
        else:
            print("Jayce nao conseguiu chegar em Piltover")
            return

        if position == "*":
            print("Jayce conseguiu chegar em Piltover")
            return
        else:
            if position in path:
                where_go = path.find(position)
            if where_go == 0:
                local[0]-=1
            elif where_go == 1:
                local[0] +=1
            elif where_go == 2:
                local[1] +=1
            elif where_go == 3:
                local[1] -=1

            position = Map[local[0]][local[1]]
            if position in portals:
                item = []
                for a in portals[position]:
                    if a != local:
                        item.append(a)
                        if where_go == 0:
                            item[0][0] -=1
                        elif where_go == 1:
                            item[0][0] +=1
                        elif where_go == 2:
                            item[0][1] +=1
                        elif where_go == 3:
                            item[0][1] -=1
                local = item[0]
        testing_the_path(Map, local, counter)
    else:
        print("Jayce nao conseguiu chegar em Piltover")
        return

if __name__ == "__main__":
    Map, Start = data_entry()
    counter = 0
    testing_the_path(Map, Start, counter)