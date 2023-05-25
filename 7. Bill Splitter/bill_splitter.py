import random

number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

current_friend_count = 0
friend_names = []
money_each = 0

try:
    if number_of_friends <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        while current_friend_count < number_of_friends:
            friend_name_input = input()
            friend_names.append(friend_name_input)
            current_friend_count += 1

        bill_value = float(input("\nEnter the total bill value:\n"))

        lucky_confirmation = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if lucky_confirmation.lower() == 'yes':
            winner = friend_names[random.randint(0, len(friend_names))]
            print(f"\n{winner} in the lucky one!\n")

            if bill_value % number_of_friends - 1 != 0:
                money_each = round(bill_value / (number_of_friends - 1), 2)
            else:
                money_each = int(bill_value / (number_of_friends - 1))

            print({friend: (money_each if friend != winner else 0) for friend in friend_names})

        elif lucky_confirmation.lower() == 'no':
            print("No one is going to be lucky\n")
            if bill_value % number_of_friends != 0:
                money_each = round(bill_value / number_of_friends, 2)
            else:
                money_each = int(bill_value / number_of_friends)
            print({element: money_each for element in friend_names})

except TypeError:
    print("Please enter the right data type.")
