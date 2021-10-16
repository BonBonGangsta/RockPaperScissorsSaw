# Rock, Paper, Scissors, and Saw! Game
# Project 3
#

# Initial Screen
# Goal: Prompt for player's names.
# restrictions: Names must be within the Minimum Size and Maximum Size set AND must be unique to each other

player1Name = ""
player2Name = ""
MAXSIZE = 20
MINSIZE = 5


# INITIAL SCREEN
# name is unique if and only if, the names are not the same regardless of capitalization
def uniqueName(p1name, p2name):
    return p1name.lower() != p2name.lower()


# a name is valid when the name's character length is more than the minimum and less than the maximum
# while also being unique
def validateName(p1name, p2name):
    return (len(p1name) > MINSIZE and len(p1name) < MAXSIZE) and uniqueName(p1name, p2name)


# get player 1's name, throw an error if name is not valid
while not validateName(player1Name, player2Name):
    player1Name = input("What is the name of the first player?")
    if not validateName(player1Name, player2Name):
        print(f"ERROR: the name entered for player 1 is not valid, name must be more than " + str(MINSIZE) + " and " +
              "less than " + str(MAXSIZE) + " characters.")

# get player 2's name, throw an error if not valid. NOTE: in the error message we call player 1 by their given name
while not validateName(player2Name, player1Name):
    player2Name = input("what is the name of the second player?")
    if not validateName(player2Name, player1Name):
        print(f"ERROR: the name entered for player 2 is not valid, name must be more than " + str(MINSIZE) + " and " +
              "less than " + str(MAXSIZE) + " characters AND must be unique compared to " + player1Name + "'s name.")

# REMINDER TO ADD THE INITIALIZATION OF ARRAYS
initializeStats()

# MENU
gameExited = False
menuText = "Please select a menu item by entering it's corresponding number and hitting enter" \
           ":\n1. Play game\n2. Show game rules\n3. Show Statistics\n4. Exit"


def exit():
    print(f"Goodbye!")
    quit()


def showMenu():
    print(menuText)


def getMenuSelection():
    validChoice = False
    while not validChoice:
        showMenu()
        choice = input()
        if '0' > choice > '4':
            print(f"ERROR: Invalid menu option entered. Please review the menu options and choose wisely")
        return choice


def menu():
    while not gameExited:
        choice = getMenuSelection()
        if choice == '1':
            print(f"Players have chosen to play the game!")
        elif choice == '2':
            print(f"Players have chosen to show the game rules.")
            rules()
        elif choice == '3':
            print(f"Players have chosen to Show Statistics.")
            stats()
        elif choice == '4':
            print(f"Players have chosen to exit the game.")
            exit()


# STATISTICS
overallStats = None
currentStats = None

def stats():
    print(player1Name + f"- Rounds Won: " + str(overallStats[0][0]) + f" Rounds Lost: " + str(overallStats[0][1])
          + f" Rounds Tied:  " + str(overallStats[0][2]))
    print(player1Name + f"- Games Won: " + str(overallStats[0][3]) + f" Games Lost: " + str(overallStats[0][4])
          + f" Games Tied:  " + str(overallStats[0][5]) + f"\n")
    print(player2Name + f"- Rounds Won: " + str(overallStats[1][0]) + f" Rounds Lost: " + str(overallStats[1][1])
          + f" Rounds Tied:  " + str(overallStats[1][2]))
    print(player2Name + f"- Games Won: " + str(overallStats[1][3]) + f" Games Lost: " + str(overallStats[1][4])
          + f" Games Tied:  " + str(overallStats[1][5]) + f"\n")
    if overallStats[0][3] > overallStats[1][3]:
        print(f"Overall human Game winner is: " + player1Name + "\n")
    elif overallStats[0][3] == overallStats[1][3]:
        print(f"There is a tie for overall human game winner!\n")
    else:
        print(f"Overall human Game winner is: " + player2Name + "\n")


def initializeStats():
    # player 1       #player 2   #computer
    overallStats = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    resetCurrentStats()


def resetCurrentStats():
    currentStats = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


def incrementPlayerStat(player, category, array):
    if array == 0:
        overallStats[player][category] += 1
    else:
        currentStats[player][category] += 1


def getStat(player, category):
    return currentStats[player][category]


# RULES

outcome = [[0, -1, 1, 1], [1, 0, -1, -1], [-1, 1, 0, -1], [-1, 1, 1, 0]]


def rules():
    print(f"Winner of the round will be determined as follows:\n"
          f"a. Rock breaks Scissors and Saw therefore Rock wins over Scissors and Saw. Rock loses against Paper.\n"
          f"b. Scissors cuts Paper therefore Scissors win over Paper. Scissors lose against Rock and Saw.\n"
          f"c. Paper covers Rock therefore Paper wins over Rock. Paper loses against Scissors and Saw.\n"
          f"d. Saw cuts through Scissors and Paper therefore Saw wins over Scissors and Paper. Saw loses against Rock.\n"
          f"e. If Player and Computer make the same selection, there is a tie.\n")


def getWinner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return 0
    else:
        return outcome[playerChoice - 1][computerChoice - 1]

# GAME

