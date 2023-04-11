# write your code here
# user_input = input('Enter cells:')
initial_game_field = '_________'

inputs = [x for x in initial_game_field]

state = ''


def print_grid():
    print('---------')
    print('| ' + inputs[0] + ' ' + inputs[1] + ' ' + inputs[2] + ' |')
    print('| ' + inputs[3] + ' ' + inputs[4] + ' ' + inputs[5] + ' |')
    print('| ' + inputs[6] + ' ' + inputs[7] + ' ' + inputs[8] + ' |')
    print('---------')


def check_and_change():
    global state
    counter = 0
    while True:
        if state != '':
            break
        else:

            inputting_coordinates = input('Enter the coordinates:')
            try:
                row, column = (int(x) for x in inputting_coordinates.split())
                if row < 1 or row > 3 or column < 1 or column > 3:
                    print('Coordinates should be from 1 to 3!')
                else:
                    my_input_field = (row - 1) * 3 + (column - 1)
                    if inputs[my_input_field] == 'X' or inputs[my_input_field] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        if counter % 2 == 0:
                            inputs[my_input_field] = 'X'
                        else:
                            inputs[my_input_field] = 'O'
                        counter += 1
                        print_grid()
                        state = (game_logic(inputs))
            except:
                print('You should enter numbers!')


def game_logic(play_field):  # clean-up the logic into more friendly solution
    a_state = ''

    winning_combinations = []
    row_1 = play_field[0:3]
    row_2 = play_field[3:6]
    row_3 = play_field[6:9]
    vertical_1 = play_field[0] + play_field[3] + play_field[6]
    vertical_2 = play_field[1] + play_field[4] + play_field[7]
    vertical_3 = play_field[2] + play_field[5] + play_field[8]
    diagonal_1 = play_field[0] + play_field[4] + play_field[8]
    diagonal_2 = play_field[2] + play_field[4] + play_field[6]

    x_row_win = row_1.count('X') == 3 or row_2.count('X') == 3 or row_3.count('X') == 3
    o_row_win = row_1.count('O') == 3 or row_2.count('O') == 3 or row_3.count('O') == 3

    x_column_win = vertical_1.count('X') == 3 or vertical_2.count('X') == 3 or vertical_3.count('X') == 3
    o_column_win = vertical_1.count('O') == 3 or vertical_2.count('O') == 3 or vertical_3.count('O') == 3

    x_diagonal_win = diagonal_1.count('X') == 3 or diagonal_2.count('X') == 3
    o_diagonal_win = diagonal_1.count('O') == 3 or diagonal_2.count('O') == 3

    if x_row_win or x_column_win or diagonal_1.count('X') == 3 or diagonal_2.count('X') == 3:
        print('X wins')
        a_state += 'win'
    elif o_row_win or o_column_win or diagonal_1.count('O') == 3 or diagonal_2.count('O') == 3:
        print('O wins')
        a_state += 'win'
    else:
        if '_' in play_field:
            pass
        else:
            print('Draw')
            a_state += 'win'
    return a_state


print_grid()

while state == '':
    check_and_change()
