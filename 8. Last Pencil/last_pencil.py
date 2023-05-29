import random
import string


def check_initial_pencil_number():
    initial_pencil_number = input("How many pencils would you like to use:\n")
    while True:

        if initial_pencil_number == '0':
            initial_pencil_number = input("The number of pencils should be positive.\n")
        elif len(initial_pencil_number) == 2:
            if list(initial_pencil_number)[0] in string.digits and list(initial_pencil_number)[1] in string.digits:
                break
            else:
                initial_pencil_number = input("The number of pencils should be numeric\n")
        elif len(initial_pencil_number) == 3:
            if list(initial_pencil_number)[0] in string.digits \
                    and list(initial_pencil_number)[1] in string.digits\
                    and list(initial_pencil_number)[2] in string.digits:
                break
            else:
                initial_pencil_number = input("The number of pencils should be numeric\n")
        elif initial_pencil_number not in string.digits or initial_pencil_number == '-':
            initial_pencil_number = input("The number of pencils should be numeric\n")
        else:
            break

    return initial_pencil_number


def check_player_name():
    global first_move
    while True:

        if first_move not in player_list:
            first_move = input("Choose between 'John' and 'Jack'\n")
        else:
            break


def check_player_take(name):
    take = input(name + "'s turn:\n")
    while True:

        if take not in "123":
            take = input("Possible values: '1', '2' or '3'\n")
        elif int(pencil_number) - int(take) < 0:
            take = input("Too many pencils were taken\n")
        else:
            break

    return take


def check_bot_take(name):
    print("Pencil number left is :" + pencil_number)

    bot_take = ''
    print(name + "'s turn:")

    if int(pencil_number) == 1:
        bot_take = '1'
    elif int(pencil_number) % 4 == 1:
        bot_take = str(random.randint(1, 3))
    elif int(pencil_number) % 4 == 0:
        bot_take = '3'
    elif int(pencil_number) % 4 == 3:
        bot_take = '2'
    elif int(pencil_number) % 4 == 2:
        bot_take = '1'

    print(bot_take)
    return bot_take


def check_win():
    if pencil_number == '0':
        if turn == "John":
            print("John won!")
        else:
            print("Jack won!")
        exit()


player_list = ["John", "Jack"]

pencil_number = check_initial_pencil_number()

first_move = input("Who will be the first (John, Jack):\n")

check_player_name()
first_player = player_list[0] if first_move == player_list[0] else player_list[1]
second_player = player_list[0] if first_move == player_list[1] else player_list[1]

turn = first_player

while True:
    print("|" * int(pencil_number))

    if turn == 'Jack':
        x = check_bot_take('Jack')
        turn = 'John'
    else:
        x = check_player_take('John')
        turn = 'Jack'

    pencil_number = str(int(pencil_number) - int(x))
    check_win()
