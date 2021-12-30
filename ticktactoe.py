import random


def createBoard():

    board = {
        "A1": " ",
        "A2": " ",
        "A3": " ",
        "B1": " ",
        "B2": " ",
        "B3": " ",
        "C1": " ",
        "C2": " ",
        "C3": " "
    }


    return board

def printBoard(board):

    print(" ",board["A1"]," | ",board["A2"]," | ",board["A3"])
    print("-------------------")
    print(" ",board["B1"]," | ",board["B2"]," | ",board["B3"])
    print("-------------------")
    print(" ",board["C1"]," | ",board["C2"]," | ",board["C3"])
    return 0

def playerTurn(board):
    

    while True:
    #Input validation.
        while True:
            userInput = input("Your turn! Pick a cell: ")
            if (userInput == "a1" or userInput == "a2" or userInput == "a3" or userInput == "b1" or userInput == "b2" or userInput == "b3" or userInput == "c1" or userInput == "c2" or userInput == "c3"):
                #Input good.
                userinput = str(userInput.upper())
                print("user input is ",userinput)
                break
            else:
                print('Invalid input. Try again.')
                continue
            
        if board[userinput] == " ":
            update = {userinput: "x"}
            board.update(update)
            return board
        else:
            print("Invalid input. Try again.")

def aiTurn(board):

    print("My turn! I'll pick a cell.")

    #AI guesses
    guesses = ["A1","A3","A2","C1","B1","B2"]

    for x in guesses:
        if board[x] == " ":
            update = {x: "o"}
            board.update(update)
            return board
        



def checkWinner(board):

    symbols = ["x","o"]

    for i in symbols:
        
        if board["A1"] == i:
            if (board["B1"] == i and board["C1"] == i):
                declareWinner(i)
            elif (board["B2"] == i and board["C3"] == i):
                declareWinner(i)
            elif (board["A2"] == i and board["A3"] == i):
                declareWinner(i)
        elif board["A2"] == i:
            if (board["B2"] == i and board["C3"] == i):
                declareWinner(i)
        elif board["A3"] == i:
            if (board["B2"] == i and board["C1"] == i):
                declareWinner(i)
            elif (board["B3"] == i and board["C3"] == i):
                declareWinner(i)
        elif board["B1"] == i:
            if (board["B2"] == i and board["B3"] == i):
                declareWinner(i)
        elif board["C1"] == i:
            if (board["C2"] == i and board["C3"] == i):
                declareWinner(i)        


def declareWinner(symbol):
    if symbol == "x":
        print("You win! Nice job.")
        exit()
    else:
        print("I win! Better luck next time.")
        exit()

def main():
    #Random who goes first.
    print("Choosing first player at random. . . .")
    randomNum = random.randint(1,2)
    if randomNum == 1:
        playersTurn = True
        print("You go first!")
    else:
        playersTurn = False
        print("I go first.")
    turnCount = 9
    board = createBoard()
    printBoard(board)

    while True:
        if playersTurn:
            board = playerTurn(board)
            playersTurn = False
        else:
            board = aiTurn(board)
            playersTurn = True

        printBoard(board)

        if turnCount >= 0:
            checkWinner(board)
            turnCount = turnCount - 1
        else:
            print("It's a draw!")
            exit()

    return 0





main()


def testLand():
    mydict = {
        "Boink": "Doink1"

    }

    print(mydict["Boink"].upper())

#testLand()

