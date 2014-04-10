from random import randint

board = []

for x in range(3):
    board.append(['_']*3)

def print_board(board):
    for row in board:
        print ('  '.join(row))

        
def win_check(player, board):
    
    count = 0

    while count < 3:
        
        row = 0
        col = 0

        # Checks the players DIAGONAL spaces 
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            print ("Backslash \ Diagonal Winner!")
            break

        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
            print ("Slash / Diagonal Winner!")
            break

        
        # Checks the players COLUMN spaces
        if board[row][count] == player and board[row + 1][count] == player and board[row + 2][count] == player:
            print ("Column " + str(count) + " Winner!" )
            break
        
        # Checks the players ROW spaces
        elif board[count][col] == player and board[count][col + 1] == player and board[count][col + 2] == player:
            print ("Row " + str(count) + " Winner!")
            break

        else:
            count += 1

# Prints out the board so the player can see
print_board(board)


def x_space(player_row, player_col):
    
    if board[player_row][player_col] == '_':
        board[player_row][player_col] = 'X'
        
    else:
        print ("Spot is already marked. Please choose another position. ")

def o_space(player_row, player_col):
    
    if board[player_row][player_col] == '_':
        board[player_row][player_col] = 'O'
        
    else:
        print ("Spot is already marked. Please choose another position. ")
        #continue

##################################################################################################################################################
### STOPPED HERE FOR TODAY! 
### FIGURE OUT HOW TO EXIT THE GAME ONCE A PLAYER HAS WON 
for turn in range(3):


    print ('')
    print ("***** PLAYER 1'S MOVE *****")
    
    player_row = int(input('Choose Row: '))
    player_col = int(input('Choose Column: '))

    x_space(player_row, player_col)
    win_check('X', board)

    print ('')
    print_board(board)
    print ('')
    
    print ("***** PLAYER 2'S MOVE *****")

    player_row = int(input('Choose Row: '))
    player_col = int(input('Choose Column: '))

    o_space(player_row, player_col)
    win_check('O', board)

    print_board(board)

    
    
