# Write your code here
import random

def show_rating(player_name):
    with open("rating.txt", "r") as file:
        for line in file:
            if player_name in line:
                rating_level = line[len(player_name) + 1:]
                break
        else:
            rating_level = 0

        return int(rating_level)


name_enter = input("Enter your name: ")
print(f"Hello, {name_enter}")

rating = show_rating(name_enter)

game_rules = input()
if not game_rules:
    game_rules = ['rock', 'paper', 'scissors']
    game_rules.reverse()
else:
    game_rules = game_rules.split(',')
    game_rules.reverse()
print("Okay, let's start")


def create_rule(rule_input):
    cnt = len(rule_input)
    rule = {}
    for idx, item in enumerate(rule_input):
        if idx + (int(len(rule_input) + 1) / 2) > cnt:
            rule[item] = rule_input[idx + 1:] + rule_input[:(int((len(rule_input) + 1) / 2)) - (cnt - idx)]
        else:
            rule[item] = rule_input[idx + 1:idx + (int((len(rule_input) + 1) / 2))]
    return rule


my_rules = create_rule(game_rules)


def game_start(user_in):
    global rating
    computer_roll = list(my_rules.keys())[random.randint(0, len(my_rules) - 1)]
    if user_input == computer_roll:
        print(f"There is a draw ({user_in})")
        rating += 50
    elif user_in in my_rules[computer_roll]:
        print(f"Sorry, but the computer chose {computer_roll}")
    elif computer_roll in my_rules[user_in]:
        print(f"Well done. The computer chose {computer_roll} and failed")
        rating += 100


while True:
    user_input = input()
    try:
        if user_input == '!exit':
            exit()
        elif user_input == '!rating':
            print(f"Your rating: {rating}")
        else:
            game_start(user_input)

    except KeyError:
        print(f"Invalid input")
