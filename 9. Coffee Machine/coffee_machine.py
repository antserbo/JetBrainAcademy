def initial_message(water, milk, coffee_beans, disposable_cups, money):
    print(f'''The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disposable_cups} of disposable cups
{money} of money''')
    return water, milk, coffee_beans, disposable_cups, money


def espresso(water, milk, coffee_beans, disposable_cups, money):
    water -= 250
    milk -= 0
    coffee_beans -= 16
    disposable_cups -= 1
    money += 4
    return water, milk, coffee_beans, disposable_cups, money


def latte(water, milk, coffee_beans, disposable_cups, money):
    water -= 350
    milk -= 75
    coffee_beans -= 20
    disposable_cups -= 1
    money += 7
    return water, milk, coffee_beans, disposable_cups, money


def cappuccino(water, milk, coffee_beans, disposable_cups, money):
    water -= 200
    milk -= 100
    coffee_beans -= 12
    disposable_cups -= 1
    money += 6
    return water, milk, coffee_beans, disposable_cups, money


def buy(water, milk, coffee_beans, disposable_cups, money):
    selection = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
    if selection == '1':
        if water < 250 or milk < 0 or coffee_beans < 16 or disposable_cups < 1:
            print('Sorry, not enough water!')
            return water, milk, coffee_beans, disposable_cups, money
        else:
            print('I have enough resources, making you a coffee!')
            return espresso(water, milk, coffee_beans, disposable_cups, money)
    elif selection == '2':
        if water < 350 or milk < 75 or coffee_beans < 20 or disposable_cups < 1:
            print('Sorry, not enough water!')
            return water, milk, coffee_beans, disposable_cups, money
        else:
            print('I have enough resources, making you a coffee!')
            return latte(water, milk, coffee_beans, disposable_cups, money)
    elif selection == '3':
        if water < 200 or milk < 100 or coffee_beans < 12 or disposable_cups < 1:
            print('Sorry, not enough water!')
            return water, milk, coffee_beans, disposable_cups, money
        else:
            print('I have enough resources, making you a coffee!')
            return cappuccino(water, milk, coffee_beans, disposable_cups, money)
    else:
        return water, milk, coffee_beans, disposable_cups, money


def fill(water, milk, coffee_beans, disposable_cups):
    water_fill = int(input('Write how many ml of water do you want to add:\n'))
    milk_fill = int(input('Write how many ml of milk do you want to add:\n'))
    beans_fill = int(input('Write how many grams of coffee beans do you want to add:\n'))
    cups_fill = int(input('Write how many disposable cups of coffee do you want to add:\n'))
    water += water_fill
    milk += milk_fill
    coffee_beans += beans_fill
    disposable_cups += cups_fill
    return water, milk, coffee_beans, disposable_cups


def take(money):
    print(f'I gave you ${money}')
    money -= money
    return money


def main():
    water, milk, coffee_beans, disposable_cups, money = 400, 540, 120, 9, 550
    while True:
        user_input = input('Write action (buy, fill, take, remaining, exit):\n')
        if user_input == 'fill':
            water, milk, coffee_beans, disposable_cups = fill(water, milk, coffee_beans, disposable_cups)
        elif user_input == 'buy':
            water, milk, coffee_beans, disposable_cups, money = buy(water, milk, coffee_beans, disposable_cups, money)
        elif user_input == 'take':
            money = take(money)
        elif user_input == 'remaining':
            initial_message(water, milk, coffee_beans, disposable_cups, money)
        elif user_input == 'exit':
            break


main()
