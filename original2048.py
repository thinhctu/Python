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
 
    # # to move down
    # elif(x == 'S' or x == 's'):
    #     mat = gamelogic.moveDown(mat)
    #     status = gamelogic.checkGameStatus(mat)
    #     print(status)
    #     if(status == 'PLAY'):
    #         gamelogic.fillTwoOrFour(mat)
    #     else:
    #         break
 
    # # to move left
    # elif(x == 'A' or x == 'a'):
    #     mat = gamelogic.moveLeft(mat)
    #     status = gamelogic.checkGameStatus(mat)
    #     print(status)
    #     if(status == 'PLAY'):
    #         gamelogic.fillTwoOrFour(mat)
    #     else:
    #         break
 
    # # to move right
    # elif(x == 'D' or x == 'd'):
    #     mat, flag = gamelogic.moveRight(mat)
    #     status = gamelogic.checkGameStatus(mat)
    #     print(status)
    #     if(status == 'PLAY'):
    #         gamelogic.fillTwoOrFour(mat)
    #     else:
    #         break
    else:
        print("Invalid Key Pressed")
 
    # print the matrix after each move

    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mat]))
