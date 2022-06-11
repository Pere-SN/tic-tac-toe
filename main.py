real_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
grid = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

player1 = {
    'name': 'Player 1',
    'choices': []}
player2 = {
    'name': 'Player 2',
    'choices': []}


def game_board(player):
    print(f"'Turn of {player['name']}, please select a position from the grid.'\n"
          f"   0    1    2\n"
          f"0{grid[0]}\n"
          f"1{grid[1]}\n"
          f"2{grid[2]}\n")
    column = int(input('Select a column:'))
    row = int(input('select a row:'))
    while column > 2 or row > 2:
        print('Please select a correct row/column between 0 and 2.')
        column = int(input('Select a column:'))
        row = int(input('select a row:'))

    if grid[row][column] == '_':
        if player == player1:
            grid[row][column] = 'O'
        else:
            grid[row][column] = 'X'
    else:
        print('Pick another square, that one is already taken!')
        game_board(player)
    player['choices'].append(real_grid[row][column])

    if player['choices'] in winning_combinations:
        print(f"{player['name']} has won!")
        reset()
    return check_board()


def check_board():
    if any('_' in row for row in grid):
        return True
    else:
        return reset()


def reset():
    repeat_match = input('The game is over do you want to play another match?\n'
                         'Type Y or N\n').upper()
    if repeat_match == 'Y':
        for row in range(3):
            for box in range(3):
                grid[row][box] = '_'
        player1['choices'] = []
        player2['choices'] = []
        return True
    else:
        print('See you soon.')
        return False


match = True
while match is True:
    if game_board(player1) is not True or game_board(player2) is not True:
        match = False
