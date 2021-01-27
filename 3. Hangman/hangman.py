import random

print('H A N G M A N')

while True:
    print('Type "play" to play the game, "exit" to quit: ', end='')
    choice = input()

    if choice == 'play':

        words = ('python', 'java', 'kotlin', 'javascript')

        secret_word = random.choice(words)
        secret_word_modified = '-' * len(secret_word)

        used_letters = set()
        my_try = 0

        while my_try < 8:
            print()
            print(secret_word_modified)
            user_guess = input('Input a letter: ')

            index_occurrences = set()

            if user_guess in used_letters:
                print('You\'ve already guessed this letter')
                continue

            if user_guess == secret_word:
                break

            if user_guess.isalpha() and len(user_guess) == 1 and user_guess.islower():
                if user_guess in secret_word:
                    for index in range(len(secret_word)):

                        if secret_word.find(user_guess, index, ) != -1:
                            index_occurrences.add(secret_word.find(user_guess, index, ))
                            used_letters.add(user_guess)

                    for index in index_occurrences:
                        secret_word_modified = secret_word_modified[:index] + user_guess + secret_word_modified[
                                                                                           index + 1:]

                elif my_try == 7 and user_guess not in secret_word:
                    my_try += 1
                    break

                else:
                    print('That letter doesn\'t appear in the word')
                    used_letters.add(user_guess)
                    my_try += 1

            if secret_word_modified == secret_word:
                break

            elif len(user_guess) != 1:
                print('You should input a single letter')

            elif not user_guess.isalpha or user_guess.islower():
                print('Please enter a lowercase English letter')

        if secret_word_modified == secret_word:
            print(f'You guessed the word {secret_word}!')
            print('You survived!')
        else:
            print('That letter doesn\'t appear in the word')
            print('You lost!')

    elif choice == 'exit':
        break

    else:
        continue
