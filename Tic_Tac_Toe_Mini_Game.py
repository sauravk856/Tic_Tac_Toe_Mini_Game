import random



def draw_board(board):
    row1 = "{}|{}|{}".format(board[0],board[1],board[2])
    row2 = f"{board[3]}|{board[4]}|{board[5]}"
    row3 = f"{board[6]}|{board[7]}|{board[8]}"

    print(row1+'\n'+row2+'\n'+row3)

def user_move(board,user_type):
    user_choice = int(input("Choose your space between 1-9: ")) - 1
    if (board[user_choice] != ' '):
        print('Space is taken, Try Again')
        user_move(board,user_type)
    else:
        board[user_choice] = user_type
        available_spaces.remove(user_choice)

def computer_move(board,user_type):
    computer_choice = random.choice(available_spaces)
    board[computer_choice] = user_type
    available_spaces.remove(computer_choice)

def check_win(board,x_o):
    a = board[0] == x_o and board[1] == x_o and board[2] == x_o
    b = board[3] == x_o and board[4] == x_o and board[5] == x_o
    c = board[6] == x_o and board[7] == x_o and board[8] == x_o
    d = board[0] == x_o and board[3] == x_o and board[6] == x_o
    e = board[1] == x_o and board[4] == x_o and board[7] == x_o
    f = board[2] == x_o and board[5] == x_o and board[8] == x_o
    g = board[0] == x_o and board[4] == x_o and board[8] == x_o
    h = board[2] == x_o and board[4] == x_o and board[6] == x_o

    res = a or b or c or d or e or f or g or h
    if res:
        play = False
        print("Hooray! {} has won".format(x_o))
    else:
        play = True
    return play



board = [" " for i in range(9)]
available_spaces = [x for x in range(9)]
draw_board(board)
play = True

comp_or_friend = input("Would you like to play against the computer or friend? (c or f): ")
while play == True:

    user_move(board,'x')
    play = check_win(board,'x')
    if play == False:
        continue
    draw_board(board)
    if comp_or_friend == 'f':
        user_move(board,'o')
    elif comp_or_friend == 'c':
        print("Computer chose")
        computer_move(board,'o')
    play = check_win(board,'o')
    draw_board(board)

print("End of the game")
