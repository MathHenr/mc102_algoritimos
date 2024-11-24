def data_entry():
    map_entry = [int(i) for i in input().split()]
    start = int(input())
    return map_entry, start

def jump(parameter, i, counter, last, direction):
    if counter < 500:
        element = parameter[i]
        if (len(parameter)/2) > i: # ESTAMOS NA ESQUERDA!
            number = i - element
            if number < 1: # CONSEGUIMOS SAIR PELA ESQUERDA!
                print('Saiu da plataforma')
                return
            else: # VERIFICANDO SE É POSSIVEL ANDAR PARA ESQUERDA!
                if parameter[number] !=0 and number != last and direction == None:  # MDODO DE ANDAR PARA QUEM COMECA NA ESQUERDA!!!
                    last = i
                    counter += 1
                    jump(parameter, i - element, counter, last, direction)
                else: 

                    
                    if parameter[number] != 0 and direction == True:
                        last = i
                        counter += 1
                        jump(parameter, i + element, counter, last, direction)

                    elif parameter[number] == 0 and element > 1:  # CONTANDO ATÉ QUANTAS CASAS CONSEGUIMOS PULAR!
                        k = False
                        while k != True:
                            element -= 1
                            number = i - element
                            if parameter[number] != 0:
                                if number != last:
                                    last = i
                                    counter += 1
                                    jump(parameter, i - element, counter, last, direction)
                                    break
                                else:
                                    break
                        if number == last: # VERIFICANDO QUE ESTAMOS INDO DA ESQUERDA PARA A DIREITA!
                            element = parameter[i]
                            direction = True
                            number = i + element
                            if parameter[number] != 0:
                                last = i
                                counter += 1
                                jump(parameter, i + element, counter, last, direction)
                            else:
                                if element > 1:
                                    k = False
                                    while k != True:
                                        element -= 1
                                        number = i + element
                                        if parameter[number] != 0:
                                            k = True
                                            break
                                    last = i
                                    counter += 1
                                    jump(parameter, i + element, counter, last, direction)
                                else:
                                    print('Loop')
                                    return # MUDAMOS DE DIREÇÃO E ACABAMOS SENDO FORÇADOS A RETORNAR (LOOP)!
                    else:

                        if element != 0: # VIRANDO PARA DIREITA, POIS NA ESUQRDA BATEREMOS EM UM ZERO!
                            number = i + element
                            if number != last:
                                if parameter[number] != 0:
                                    last = i
                                    counter += 1
                                    jump(parameter, i + element, counter, last, direction)
                                else: # BATEREMOS EM UM ZERO PELA ESQUERDA E PELA DIREITA!
                                    print('Loop')
                                    return
                            # NUMBER DIFERENTE DE LAST!!!!!
                            
                        else: # ESTAMOS EM UM ZERO!
                            print('Loop')
                            return
        else: # ESTAMOS PARA A DIREITA
            number = i + element
            if number >= len(parameter): # SIGNIFICA QUE CONSEGUIMOS SAIR PELA DIREITA!
                print('Saiu da plataforma')
                return
            else: # VERIFICANDO SE É POSSIVEL ANDA PARA DIREITA!
                if parameter[number] != 0 and number != last and direction == None:
                    last = i
                    counter += 1
                    jump(parameter, i + element, counter, last, direction)
                else:


                    if parameter[number] != 0 and direction == False: # CONTANDO QUANTAS CASAS CONSEGUIMOS PULAR!
                        last = i
                        counter += 1
                        jump(parameter, i - element, counter, last, direction)

                    elif parameter[number] == 0 and element > 1:
                        k = False
                        while k != True:
                            element -= 1
                            number = i + element
                            if parameter[number] != 0:
                                if number != last:
                                    k = True
                                    last = i
                                    counter += 1
                                    jump(parameter, i + element, counter, last, direction)
                                    break
                                else:
                                    break



                        if number == last:
                            element = parameter[i]
                            direction = False
                            number = i - element  # VERIFICANDO QUE ESTAMOS INDO DA DIREITA PARA ESQUERDA!
                            if parameter[number] != 0:
                                last = i
                                counter += 1
                                jump(parameter, i - element, counter, last, direction)
                            else:
                                if element > 1:
                                    k = False
                                    while k != True:
                                        element -= 1
                                        number = i - element
                                        if parameter[number] != 0:
                                            k = True
                                            break
                                    last = i
                                    counter += 1
                                    jump(parameter, i - element, counter, last, direction)
                                else:
                                    print('Loop')
                                    return # MUDAMOS DE DIRECAO E ACABAMOS SENDO FORÇADOS A RETORNANAR (LOOP)!       




                    else:
                        if element != 0:
                            if direction ==  True:
                                number = i + element
                                if number != last:
                                    if parameter[number] != 0:
                                        last = i
                                        counter += 1
                                        jump(parameter, i + element, counter, last, direction)
                                    else:
                                        print('Loop')
                                        return
                                else:
                                    print('Loop')
                                    return
                            
                            else:
                                number = i - element
                                if number != last:
                                    if parameter[number] != 0:
                                        last = i
                                        counter += 1
                                        jump(parameter, i - element, counter, last, direction)
                                    else:
                                        print('Loop')
                                        return  # BATEREMOS EM UM ZERO PELA DIREITA E PELA ESQUERDA!
                                # Number diferente de last!!!
                        else:
                            print('Loop')
                            return # ESTAMOS EM UM ZERO!




    else:
        print('Loop')
        return # EXCEDEMOS O COUNTER!


if __name__ == "__main__":
    parameter, i = data_entry()
    counter = 0
    last = None
    direction = None
    jump(parameter, i-1, counter, last, direction)