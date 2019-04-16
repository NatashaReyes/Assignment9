#Natasha Reyes - Assignment 9

from random import randint
board = [ ]





#This function creates the gameboard
def battleBoard(board):
    for row in board:
        print(' '.join(row))
        

print("Hello! This is a Battleship program! The goal of the game is to sink the enemy ship! ")
#This for loop will construct the list needed for the board
for i in range(5):
    board.append(["O"]* 5)
    
    
battleBoard(board)
#functions that help place the enemy ship on the board and input to have you guess
def randomBoardRow(board):
    return randint(0,len(board)-1)

def randomBoardCol(board):
    return randint(0,len(board)-1)

ship_row = randomBoardRow(board)
ship_col = randomBoardCol(board)

#User input on how they guess enemy ship location


for turn in range(4):
    print ("Turn"), turn + 1
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sank the enemy battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print ("Oops, that's not even in the range...")
        elif board[guess_row][guess_col] == "X":
            print( "You guessed that one already..." )
        else:
            print ("You missed the enemy battleship!")
            board[guess_row][guess_col] = "X"
        if (turn == 4):
            print ("Game Over")
            break
    battleBoard(board)
    