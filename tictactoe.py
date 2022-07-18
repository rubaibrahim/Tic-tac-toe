import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Take player input

def playerInput(board):
    inp = int(input("Enter a number between 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("oops already taken :)")


# Check for win or tie

def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkRows(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True

    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True

    elif board[2] == board[8] == board[5] and board[5] != "-":
        winner = board[5]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[4]
        return True

    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        return True


def checkWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False

    elif checkRows(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# Switch the player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)
