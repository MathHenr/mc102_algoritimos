import random as rd
def main():

    ready = player_ready()

# Verificando se houve alguma duvida com as regras do jogo
    while ready == False:
        ready = player_ready()
        if ready == True:
            playing_game()
            break
# Perguntando ao jogador qual estilo de jogo ele quer jogar
    method = player_chose_method()

# Jogando
    playing_game(method)
            
            
def playing_game(method):
    if method > 1:
        # Pegando valores escolhidos pelo usuário
        number_1, number_2 = picking_numbers()

        if number_1 == number_2:
            number_1, number_2 = requirement_number_chosen_two(number_1, number_2)

        # Pegando valor aleatório entre os números escolhidos pelo usuário
        chosen_number = rd.randint(number_1, number_2)

        correct_answer = False

        # Tentativas até o acerto
        attempts = 1

        while correct_answer == False:
            guess = int(input(f"Chute um valor entre {number_1} e {number_2}: ---> "))

            if guess == chosen_number:
                if attempts > 1:
                    alert_attempts = "tentativas"
                else:
                    alert_attempts = "tentativa"

                print(f"Parabéns você acertou o número em {attempts} {alert_attempts}.")
                correct_answer = True
                break
            else:
                if guess > chosen_number:
                    print(f"{guess} é maior que o número aleatório!")
                else:
                    print(f"{guess} é menor que o número aleatório!")

                attempts+=1
    else:
        # Pegando valor maximo inserido pelo usuario
        number_1 = int(input("Digite um número: "))

        if number_1 == 0:
            number_1= requirement_number_chosen_one(number_1)

        chosen_number = rd.randint(0, number_1)

        correct_answer = False

        # Tentativas até o acerto
        attempts = 1

        while correct_answer == False:
            guess = int(input(f"Chute um valor entre 0 e {number_1}: ---> "))

            if guess == chosen_number:
                if attempts > 1:
                    alert_attempts = "tentativas"
                else:
                    alert_attempts = "tentativa"

                print(f"Parabéns você acertou o número em {attempts} {alert_attempts}.")
                correct_answer = True
                break
            else:
                if guess > chosen_number:
                    print(f"{guess} é maior que o número aleatório!")
                else:
                    print(f"{guess} é menor que o número aleatório!")

                attempts+=1


def player_chose_method():
    one_number = str(input("Voce gostaria de escoher apenas o número máximo: ---> "))
    if one_number == "s":
        return 1
    else:
        return 2


def player_ready():
    # Lendo as regras dp jogo para o usuario

    print("----------- BEM VINDO AO GUESS THE NUMBER ------------")
    print("****Os números são escolhidos de forma aleatória****") 
    print("----- Você escolhe o número limite para o sorteio, por exemplo -----")
    print("----- Digite s para sim e n para não -----")
    print("----- Você digita 10, e os números sorteados seram os números dentre 0 e 10 -----")
    print("----- Você também pode digitar o menor valor limite para sortear os números -----")
    answer_1 = str(input("----- Você entendeu as regras? -----> "))

    if answer_1 == "s":
        return True
    else:
        return False


def picking_numbers():
    number_1 = int(input("Digite um número inteiro: "))
    number_2 = int(input("Digite um número, inteiro, maior que o número anterior: "))
    return number_1, number_2


def requirement_number_chosen_one(argument):
    # Verificando se o número colocado pleo usaurio é maior que 0

    while argument <= 0:
        number_1 = int(input("Por favor, digite um número positivo maior que 0: "))
        if number_1 > 0:
            return number_1

def requirement_number_chosen_two(argument1, argument2):
    # Verificando se os valores inseridos são diferentes
    while argument1 == argument2:
        number_1 = int(input("Digite um número inteiro: "))
        number_2 = int(input("Digite um número maior que o número anterior e que seja DIFERENTE do primeiro valor: "))
        if number_1 != number_2 and number_2 > number_1:
            return number_1, number_2

main()