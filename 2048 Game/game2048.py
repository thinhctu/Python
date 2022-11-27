import gamelogic
 
# Driver code
     
#initializing matrix
if __name__ == '__main__':
    mat = gamelogic.initialize()

while(True):
 
    x = input("Press the command : ")
 
    if(x == 'W' or x == 'w' or x == 'A' or x == 'a' or x == 'S' or x == 's' or x == 'D' or x == 'D'):
        mat = gamelogic.move(x, mat)
        # get the current state and print it
        status = gamelogic.checkGameStatus(mat)
        print(status)
        # if game not over then continue and add tile
        if(status == 'PLAY'):
            gamelogic.fillTwoOrFour(mat)
        # else break the loop
        else:
            break
    else:
        print("Invalid Key Pressed")
 
    # print the matrix after each move

    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mat]))
