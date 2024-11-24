def data_entry():
    map_entry = [int(i) for i in input().split()]
    start_position = int(input())
    return map_entry, start_position

def jump(argument, i, path, direction, repet):
    if repet < 200:
        item = argument[i]
        argumentLeng = len(argument)
        if (argumentLeng/2) > i: # Significa que estamos mais perto de sair pela esquerda!
            jumpNumber = i - item
            if jumpNumber < 0:
                print('Saiu da plataforma') # Return True
            elif path == True and direction == 'left': # Com o path nas condicoes verificamos se precisamos mudar de lado sem cair em um loop
                jumpNumber = i - item
                if argument[jumpNumber] != 0:
                    repet+=1
                    jump(argument, i - item, path, direction, repet)
                else:
                    counter = False
                    while counter == False:
                        if item != 0:
                            item +=1
                            jumpNumber = i - item
                            if argument[jumpNumber] != 0:
                                counter = True
                                break
                        else:
                            print('Loop')
                            return False
                    repet+=1
                    jump(argument, i - item, path, direction, repet)
            elif path == True and direction == 'right':
                jumpNumber = i + item
                if argument[jumpNumber] != 0:
                    repet+=1
                    jump(argument, i + item, path, direction, repet)
                else:
                    counter = False
                    while counter == False:
                        if item != 0:
                            item -=1
                            jumpNumber = i + item
                            if argument[jumpNumber] != 0:
                                counter = True
                                break
                        else:
                            print('Loop')
                            return False
                    repet+=1
                    jump(argument, i + item, path, direction, repet)
            else:
                if argument[jumpNumber] == 0:
                    if item > 1:
                        counter = False
                        while counter == False:
                            item -=1
                            jumpNumber = i - item
                            if argument[jumpNumber] != 0:
                                counter = True
                                break
                        repet+=1
                        jump(argument, i - item, path, direction, repet)
                    else:
                        path = True
                        direction = 'right'
                        repet+=1
                        jump(argument, i + item, path, direction, repet)
                else:
                    repet+=1
                    jump(argument, i - item, path, direction, repet)

        elif (argumentLeng/2) < i: # Significa que estamos mais perto de sair pela direita!
            jumpNumber = i + item
            if jumpNumber >= argumentLeng:
                print('Saiu da plataforma') # Return True
            elif path == True and direction == 'left': # Com o path nas condicoes verificamos se precisamos mudar de lado sem cair em um loop
                jumpNumber = i - item
                if argument[jumpNumber] != 0:
                    repet+=1
                    jump(argument, i- item, path, direction, repet)
                else:
                    counter = False
                    while counter == False:
                        if item != 0:
                            item +=1
                            jumpNumber = i - item
                            if argument[jumpNumber] != 0:
                                counter = True
                                break
                        else:
                            print('Loop')
                            return False
                    repet+=1
                    jump(argument, i - item, path, direction, repet)
            elif path == True and direction == 'right':
                jumpNumber = i + item
                if argument[jumpNumber] != 0:
                    repet+=1
                    jump(argument, i + item, path, direction, repet)
                else:
                    counter = False
                    while counter == False:
                        if item != 0:
                            item -=1
                            jumpNumber = i + item
                            if argument[jumpNumber] != 0:
                                counter = True
                                break
                        else:
                            print('Loop')
                            return False
                    repet+=1
                    jump(argument, i + item, path, direction, repet)
            else:
                if argument[jumpNumber] == 0 :
                    if item > 1:
                        counter = False
                        while counter == False:
                            item +=1
                            jumpNumber = i - item
                            if argument[jumpNumber] != 0:
                                counter = True
                                break
                            repet+=1
                            jump(argument, i - item, path, direction, repet)
                    else:
                        path = True
                        direction = 'left'
                        repet+=1
                        jump(argument, i - item, path, direction, repet)
                else:
                    repet+=1
                    jump(argument, i + item, path, direction, repet)
    else:
        print('Loop')

if __name__ == "__main__":
    parameter, i = data_entry()
    path = False
    direction = None
    repet = 0
    jump(parameter, i-1, path, direction, repet)