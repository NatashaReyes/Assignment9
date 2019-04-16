garden = [ ]

#This function creates the garden

def gardenBuild(garden):
    for row in garden:
        print(' '.join(row))
        

print("Welcome to Pluck and Plant! In this game, you are removing and planting flowers! ")
#for loop for garden
for i in range(5):
    garden.append(["|"]* 5)
    
    
gardenBuild(garden)


#This keeps the user in the game for four turns
for turn in range(4):
    print ("Turn"), turn + 1
    move_row = int(input("Move Row: "))
    move_col = int(input("Move Column: "))
    
    if move_row in range(5) and move_col in range(5):
        doPlant = int(input( "Would you like to plant a flower here? (1 = Yes /2 =  No)"))
        if(doPlant == 1):
            garden[move_row][move_col] = "⚘"
            print("You planted a flower!")
            gardenBuild(garden)
        else: 
            move_row = int(input("Move Row: "))
            move_col = int(input("Move Column: "))
        
    if move_row not in range(5) or move_col not in range(5):
        print ("Oops, that's not even in the range...")
    elif garden[move_row][move_col] == "⚘":
        userChoice = int(input( "There is already a flower here! Would you like to remove it? (1 = Yes /2 =  No)"))
        if(userChoice == 1):
            garden[move_row][move_col] = "|"
            print("You plucked the flower!")     
        if (turn == 4):
            print ("Game Over!")
            break
    else:
        print("")
    gardenBuild(garden)
    