from IPython.display import clear_output


def user_input():
    user_move = 0
    chk = True
    while chk:
        try:
            user_move = int(input("Go with your move(0-8)"))
        except :
            print("Expected number 0-8")
        else:
            break
    return user_move


def print_board(player_moves):
    clear_output(wait=False)
    moves = 0
    length = len(player_moves)
    for i in range(0, 3):
        for j in range(0, 3):
            print(player_moves[moves+j] + "  |  ", end=" ")
        print("\n_____________________")
        moves += 3


def check_game_over(player_moves):
    game_over = False
    # checking cases in all rows
    if player_moves[0] == player_moves[1] == player_moves[2] and player_moves[0] != ' ':
        game_over = True
    if player_moves[3] == player_moves[4] == player_moves[5] and player_moves[3] != ' ':
        game_over = True
    if player_moves[6] == player_moves[7] == player_moves[8] and player_moves[6] != ' ':
        game_over = True
    if player_moves[0] == player_moves[3] == player_moves[6] and player_moves[0] != ' ':
        game_over = True
    if player_moves[1] == player_moves[4] == player_moves[7] and player_moves[1] != ' ':
        game_over = True
    if player_moves[2] == player_moves[5] == player_moves[8] and player_moves[2] != ' ':
        game_over = True
    if player_moves[0] == player_moves[4] == player_moves[8] and player_moves[0] != ' ':
        game_over = True
    if player_moves[2] == player_moves[4] == player_moves[6] and player_moves[2] != ' ':
        game_over = True
    return game_over


def player(next_player):
    if next_player is True:
        return False
    else:
        return True


def position_check(player_moves, move):
    if player_moves[move] == ' ':
        return True
    else:
        print("Prohibited!!")
        return False


moves_list = [' ']*9
game = True  # game over indicating flag
print("Player 1 = X")
print("Player 2 = O")
print("Player 1 will start.")
player_turn = True
max_moves = 0
while game:
    print_board(moves_list)
    max_moves += 1
    if player_turn is True:
        sym = 'X'
        print("Player1's Turn")
    else:
        sym = 'O'
        print("Player2's Turn")
    correct_move = True
    while correct_move:
        current_move = user_input()
        if position_check(moves_list, current_move) is True:
            moves_list[current_move] = sym
            break
    if check_game_over(moves_list) is True:
        print_board(moves_list)
        print("Game Over!!")
        game = False
    player_turn = player(player_turn)
    if max_moves == 9 and game is not False:
        print("Game Tied!!")
        game = False
    if game is False:
        ask = str(input("Do you like to play again? (y/n)"))
        if ask == 'y' or ask == 'Y':
            game = True
            del moves_list
            moves_list = [' ']*9
            player_turn = True
            max_moves = 0



