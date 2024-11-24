import random as rd
# Iniciando o jogo através dp usuário
def main():
    #user = user_wants_play()

    user_pick = teaching_rules()
    winner(user_pick)

'''
def user_wants_play():
    print("Bem vindo ao jogo Pedra, Papel e Tesoura, responda s para sim e n para não")
    want_platy = str(input("Quer jogar Pedra, Papel e Tesoura? ---> "))

    if want_platy == s:
        return True
    else:
        return False
'''

def teaching_rules():
    print("Escolha uma das opcoes abaixo para jogar:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    user_pick = int(input(">> "))

    return user_pick

def winner(argument):
    if argument != 0 and argument in range(4):
        random_choise = rd.randint(0,3)

        list_item = ["pedra", "papel", "tesoura"]

        if random_choise == 1 and argument == 3:
            print(f"Você ganhou !! Escolheu {list_item[argument - 1]} contra {list_item[random_choise - 1]} !!")
        else:
            if random_choise == 2 and argument == 3:
                print(f"Você ganhou !! Escolheu {list_item[argument - 1]} contra {list_item[random_choise - 1]} !!")
            else:
                if random_choise == 3 and argument == 1:
                    print(f"Você ganhou !! Escolheu {list_item[argument - 1]} contra {list_item[random_choise - 1]} !!")
                else:
                    if random_choise != argument:
                        print(f"Você perdeu !! Escolheu {list_item[argument - 1]} contra {list_item[random_choise - 1]}!!")
                    else:
                        print(f"Empate !! Tivemos {list_item[argument - 1]} contra {list_item[random_choise - 1]}!!")

        again = play_again()

        if again == True:
            main()


def play_again():
    quest = str(input("Quer jogar de novo? --> "))
    
    if quest == "s":
        return True
    else:
        return False

main()