# DomirScire

import itertools

def win(current_game):
    def all_same(l, sth):
        if l.count(l[0]) == len(l) and l[0] != 0:
            print(f"{sth} is the winner!")
            return True
        else:
            return False

    # Horizontal
    for row in game:
        print(row)
        if all_same(row, row):
            return True

    # Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags, diags):
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags, diags):
        return True

    # Vertical
    for col in range(len(game)):
        check=[]
        for row in game:
            check.append(row[col])
        if all_same(check, check):
            return True

    return False

P = 'User_1'
C = 'User_2'
players = [P, C]

def game_board(game_map, player='User_1', row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupated! Choose another one!")
            return game_map, False

        print("   "+"  ".join([str(i) for i in range(len(game_map))]))

        if not just_display:
            if player == 'User_1':
                game_map[row][column] = 'X'
            if player == 'User_2':
                game_map[row][column] = 'O'

        for count, row in enumerate(game_map):
            print(count, row)

        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column in range?", e)
        return game_map, False

    except Exception as e:
        print("Something went Wrong!, e")
        return game_map, False

play = True
while play:
    game_size = int(input("Input the size of the game: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle([P,C])

    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column?"))
            row_choice = int(input("What row?"))
            game, played = game_board(game, current_player,row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) \n")

            if again.lower() == "y":
                print("restarting")
            else:
                print("Bye")
                play = False
