#initial game variables
gameStart = [["+","+","+"],["+","X","+"],["+","+","+"]]
blackList = [["+","+","+"],["+","X","+"],["+","+","+"]]
player = "Start"
row = 0
column = 0
#player input
def gameBoard(player, row, column):
    if player == "Start":
        print("    0    1    2")
        for count, row in enumerate(gameStart):
            print(count,row)
    if player != "Start":
        try: 
            if blackList[row][column] != "+":
                for count, row in enumerate(gameStart):
                    print(count,row)
                print("select another position. that one is taken.")
                if player == "O":
                    playerMove()
                if player == "X":
                    aiMove()
            if blackList[row][column] == "+":
                gameStart[row][column] = player
                blackList[row][column] = player
                print("    0    1    2")
                for count, row in enumerate(gameStart):
                    print(count,row)
        except IndexError:
            print("possible options are 0, 1, and 2.")
            if player == "O":
                playerMove()
            if player == "X":
                aiMove()
        except Exception:
            print("Something went wrong.")
            if player == "O":
                playerMove()
            if player == "X":
                aiMove()
#players move
def playerMove():
    player = "O"
    print("O: Select a Row... ")
    try:
        row = int(input())
    except ValueError:
        print("possible options are 0, 1, and 2.")
        playerMove()
        exit()
    print("O: Select a Column... ")
    try:
        column = int(input())
    except ValueError:
        print("possible options are 0, 1, and 2.")
        playerMove()
        exit()
    gameBoard(player, row, column)
    checkWinner()
    aiMove()
#ais move
def aiMove():
    player = "X"
    print("X: Select a Row... ")
    try:
        row = int(input())
    except ValueError:
        print("possible options are 0, 1, and 2.")
        playerMove()
        exit()
    print("X: Select a Column... ")
    try:
        column = int(input())
    except ValueError:
        print("possible options are 0, 1, and 2.")
        playerMove()
        exit()
    gameBoard(player, row, column)
    checkWinner()
    playerMove()
#compare
def compare(l):
    if l.count(l[0]) == len(l) and l[0] != "+":
        print("Winner!")
        resetGame()
#check for winner
def checkWinner():
    #horizontal winner
    for row in gameStart:
        compare(row)
    #vertical winner
    for col in range(len(gameStart)):
        verticalWinCheck = []
        for row in gameStart:
            verticalWinCheck.append(row[col])
        compare(verticalWinCheck)
    #diagonal winner
    diags = []
    for index in range(len(gameStart)):
        diags.append(gameStart[index][index])
    compare(diags)
    diags = []
    for col, row in enumerate(reversed(range(len(gameStart)))):
        diags.append(gameStart[row][col])
    compare(diags)
#reset game after winner
def resetGame():
    print("Would you like to play again?... (y/n): ")
    answer = input()
    if answer != "y" and answer != "n":
        print("Press y to reset game, press n to quit")
        resetGame()
        exit()
    if answer == "y":
        print("Reset game does not currently reset the game board... quitting...")
        quit()
        #print("lets play a game")
        #print("you are O")
        #print("ai is X")
        #gameBoard(player, row, column)
        #playerMove()
    if answer == "n":
        print("Cya later!")
        quit()

#show initial board state and start game
print("lets play a game")
print("you are O")
print("ai is X")
gameBoard(player, row, column)
playerMove()
