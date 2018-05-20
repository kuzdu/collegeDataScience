import sys
import random


def showCurrentMatchField():
    for field in ticTacToeFields:
        print(field)
    return


def isInputNumberInValidRange(number):
    if 0 <= number <= 2:
        return True
    else:
        print("Invalid number: Please enter 0,1 or 2")
        return False


def readUsersInput():
    console_input = sys.stdin.readline()

    while True:
        try:
            console_input_to_int = int(console_input)
            if isInputNumberInValidRange(console_input_to_int):
                return console_input_to_int
            else:
                console_input = sys.stdin.readline()
        except ValueError:
            print("It's not a number. Please enter numbers between 0-2")
            console_input = sys.stdin.readline()


def togglePlayerSign(player_sign):
    if player_sign == 1:
        return 2
    else:
        return 1


# I know it's a really stupid algorithms but I think for a Tic Tac Toe demo it's okay. ¯\_(ツ)_/¯
# player_sign can be is 1 or 2
def isThereAWinner(input_player_sign):
    # horizontal check

    if ticTacToeFields[0][0] == input_player_sign and \
            ticTacToeFields[0][1] == input_player_sign and \
            ticTacToeFields[0][2] == input_player_sign:
        return True
    elif ticTacToeFields[1][0] == input_player_sign and \
            ticTacToeFields[1][1] == input_player_sign and \
            ticTacToeFields[1][2] == input_player_sign:
        return True
    elif ticTacToeFields[2][0] == input_player_sign and \
            ticTacToeFields[2][1] == input_player_sign and \
            ticTacToeFields[2][2] == input_player_sign:
        return True

    # vertical check
    if ticTacToeFields[0][0] == input_player_sign and \
            ticTacToeFields[1][0] == input_player_sign and \
            ticTacToeFields[2][0] == input_player_sign:
        return True
    elif ticTacToeFields[1][0] == input_player_sign and \
            ticTacToeFields[1][1] == input_player_sign and \
            ticTacToeFields[1][2] == input_player_sign:
        return True
    elif ticTacToeFields[2][0] == input_player_sign and \
            ticTacToeFields[2][1] == input_player_sign and \
            ticTacToeFields[2][2] == input_player_sign:
        return True

    # diagonal check
    if ticTacToeFields[0][0] == input_player_sign and \
            ticTacToeFields[1][1] == input_player_sign and \
            ticTacToeFields[2][2] == input_player_sign:
        return True
    elif ticTacToeFields[2][0] == input_player_sign and \
            ticTacToeFields[1][1] == input_player_sign and \
            ticTacToeFields[0][2] == input_player_sign:
        return True

    return False


def isDraw():
    for field in ticTacToeFields:
        for innerField in field:
            if innerField == 0:
                return False
    return True


def isFieldFree(row, column):
    return ticTacToeFields[row][column] == 0


def setChoice(row, column, player_sign):
    ticTacToeFields[row][column] = player_sign
    return


def kiMakeMove():
    get_column = random.randint(0, len(ticTacToeFields) - 1)
    get_row = random.randint(0, len(ticTacToeFields[get_column]) - 1)

    if isFieldFree(get_row, get_column):
        print("---------------")
        print("KI thinks, KI will beat you.")
        setChoice(get_row, get_column, 2)
        return True

    kiMakeMove()


def isHuman(player_sign):
    if player_sign == 1:
        return True
    return False


def isEnd(player_sign):
    if isThereAWinner(player_sign):
        print("Player", player_sign, "wins: congratulation")
        showCurrentMatchField()
        return True
    elif isDraw():
        print("It's a draw. You're both very bad or very good players. Nobody knows it...")
        showCurrentMatchField()
        return True
    return False


# Main Program
ticTacToeFields = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("Player 1 starts. Please add a number between 0-2")
player_sign = 1

while True:

    showCurrentMatchField()

    if isHuman(player_sign):
        print("Please enter column between 0-2 and row between 0-2")
        print("It's your turn player ", player_sign)
        print("Column:")
        column = readUsersInput()
        print("Row:")
        row = readUsersInput()

        if isFieldFree(row, column):
            setChoice(row, column, player_sign)

            if isEnd(player_sign):
                break

            player_sign = togglePlayerSign(player_sign)
        else:
            print("Come on player", player_sign, ". Please choose a free field.")
    else:
        kiMakeMove()
        if isEnd(player_sign):
            break
        player_sign = togglePlayerSign(player_sign)