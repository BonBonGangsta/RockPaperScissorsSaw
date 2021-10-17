# Rock, Paper, Scissors, and Saw! Game
# Project 3
#
# imports
import random

## Variables
# Initial Screen
player1Name = ""
player2Name = ""
MAXSIZE = 20
MINSIZE = 5
# MENU
gameExited = False
menuText = "Please select a menu item by entering it's corresponding number and hitting enter" \
           ":\n1. Play game\n2. Show game rules\n3. Show Statistics\n4. Exit"
# STATISTICS
overallStats = None
currentStats = None
# RULES
outcome = [[0, -1, 1, 1], [1, 0, -1, -1], [-1, 1, 0, -1], [-1, 1, 1, 0]]

# Initial Screen Module

def uniqueName(p1name, p2name):
    return p1name.lower() != p2name.lower()


# a name is valid when the name's character length is more than the minimum and less than the maximum
# while also being unique
def validateName(p1name, p2name):
    return (len(p1name) > MINSIZE and len(p1name) < MAXSIZE) and uniqueName(p1name, p2name)

def getNames():
    global player1Name
    global player2Name
    # get player 1's name, throw an error if name is not valid
    while not validateName(player1Name, player2Name):
        player1Name = input("What is the name of the first player?\n")
        if not validateName(player1Name, player2Name):
            print(f"ERROR: the name entered for player 1 is not valid, name must be more than " + str(MINSIZE) + " and " +
                  "less than " + str(MAXSIZE) + " characters.\n")

    # get player 2's name, throw an error if not valid. NOTE: in the error message we call player 1 by their given name
    while not validateName(player2Name, player1Name):
        player2Name = input("what is the name of the second player?\n")
        if not validateName(player2Name, player1Name):
            print(f"ERROR: the name entered for player 2 is not valid, name must be more than " + str(MINSIZE) + " and " +
                  "less than " + str(MAXSIZE) + " characters AND must be unique compared to " + player1Name + "'s name.\n")

## Menu Module
# exit the menu and say Goodbye
def exit():
    print(f"Goodbye!")
    quit()

# prints the menuText when called
def showMenu():
    print(menuText)

# print the menu and retrieve the players choice, if an invalid choice is given, give an error
def getMenuSelection():
    validChoice = False
    while not validChoice:
        showMenu()
        choice = input()
        if choice not in ['1','2', '3', '4']:
            print(f"ERROR: Invalid menu option entered. Please review the menu options and choose wisely")
        validChoice = True
        return choice

# this will control which other functions to call. While the menu is not exited, return to the menu.
def menu():
    while not gameExited:
        choice = getMenuSelection()
        if choice == '1':
            print(f"Players have chosen to play the game!")
            play()
        elif choice == '2':
            print(f"Players have chosen to show the game rules.")
            rules()
        elif choice == '3':
            print(f"Players have chosen to Show Statistics.")
            stats()
        elif choice == '4':
            print(f"Players have chosen to exit the game.")
            exit()

## Statistics Module

# prints out the players statistics in one line while also announcing the overall game winner.
def stats():
    print(player1Name + f"- Rounds Won: " + str(overallStats[0][0]) + f" Rounds Lost: " + str(overallStats[0][1])
          + f" Rounds Tied:  " + str(overallStats[0][2]) + f" Games Won: " + str(overallStats[0][3]) +
          f" Games Lost: " + str(overallStats[0][4]) + f" Games Tied:  " + str(overallStats[0][5]) + f"\n")
    print(player2Name + f"- Rounds Won: " + str(overallStats[1][0]) + f" Rounds Lost: " + str(overallStats[1][1])
          + f" Rounds Tied:  " + str(overallStats[1][2]) + f" Games Won: " + str(overallStats[1][3]) +
          f" Games Lost: " + str(overallStats[1][4]) + f" Games Tied:  " + str(overallStats[1][5]) + f"\n")
    if overallStats[0][3] > overallStats[1][3]:
        print(f"Overall human Game Winner is: " + player1Name + "\n")
    elif overallStats[0][3] == overallStats[1][3]:
        print(f"Players tie for overall Game Wins!\n")
    else:
        print(f"Overall human Game Winner is: " + player2Name + "\n")


def initializeStats():
    global overallStats
    overallStats = [ [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0] ]
    resetCurrentStats()


def resetCurrentStats():
    global currentStats
    currentStats = [ [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0] ]


def incrementPlayerStat(player, category, array):
    if array == 0:
        overallStats[player][category] += 1
    else:
        currentStats[player][category] += 1


def getStat(player, category):
    return currentStats[player][category]



## Rules Module

def rules():
    print(f"Winner of the round will be determined as follows:\n"
          f"a. Rock breaks Scissors and Saw therefore Rock wins over Scissors and Saw. Rock loses against Paper.\n"
          f"b. Scissors cuts Paper therefore Scissors win over Paper. Scissors lose against Rock and Saw.\n"
          f"c. Paper covers Rock therefore Paper wins over Rock. Paper loses against Scissors and Saw.\n"
          f"d. Saw cuts through Scissors and Paper therefore Saw wins over Scissors and Paper. Saw loses against Rock.\n"
          f"e. If Player and Computer make the same selection, there is a tie.\n")

def getWinner(playerChoice, computerChoice):
    return outcome[(playerChoice - 1)][(computerChoice - 1)]

# GAME

def play():
    stopPlaying = False
    chooseYourWeapon = 'What weapon will you choose? "1" Rock, "2" Paper, "3" Scissors, or "4" Saw\n'
    p1WoC = None
    p2WoC = None
    compWoC = None
    while not stopPlaying:
        for i in range(1,4):
            p1ValidChoice = False
            while not p1ValidChoice:
                p1WoC = int(input(player1Name + ", " + chooseYourWeapon))
                if not p1WoC in range(1,5):
                    print("ERROR:invalid selection. " + player1Name + ", " + chooseYourWeapon)
                p1ValidChoice = True
            p2ValidChoice = False
            while not p2ValidChoice:
                p2WoC = int(input(player2Name + ", " + chooseYourWeapon))
                if not p2WoC in range(1,5):
                    print("ERROR:invalid selection. " + player2Name + ", " + chooseYourWeapon)
                p2ValidChoice = True
            compWoC = random.randint(1,4)
            calculateWinnerofRound(player1Name, 0, p1WoC, compWoC)
            calculateWinnerofRound(player2Name, 1, p2WoC, compWoC)
        gameWinner()
        resetCurrentStats()
        stopPlaying = not continuePlaying()


def calculateWinnerofRound(playerName, playerRow, playerChoice, computerChoice):
    if(getWinner(playerChoice,computerChoice)) == 0: # if player and computer choose the same weapon it's a tie
        print(playerName + " has chosen " + getWeaponFromChoice(playerChoice) + " and computer has chosen " + getWeaponFromChoice(computerChoice) + " winner: tie!\n")
        incrementPlayerStat(playerRow, 2, 0) # increment the player's stat for round ties on overall stats
        incrementPlayerStat(playerRow, 2, 1) # increment the player's stat for round ties in current game
        incrementPlayerStat(2,2,1) # increment the computer's stat for round ties in current game
    elif(getWinner(playerChoice,computerChoice)) > 0:
        print(playerName + " has chosen " + getWeaponFromChoice(playerChoice) + " and computer has chosen " + getWeaponFromChoice(computerChoice) + " winner: "+ playerName +"!\n")
        incrementPlayerStat(playerRow, 0, 0)  # increment the player's stat for round wins on overall stats
        incrementPlayerStat(playerRow, 0, 1)  # increment the player's stat for round wins in current game
        incrementPlayerStat(2, 1, 1)  # increment the computer's stat for round loss in current game
    else:
        print(playerName + " has chosen " + getWeaponFromChoice(playerChoice) + " and computer has chosen " + getWeaponFromChoice(computerChoice) + " winner: Computer!\n")
        incrementPlayerStat(playerRow, 1, 0)  # increment the player's stat for round wins on overall stats
        incrementPlayerStat(playerRow, 1, 1)  # increment the player's stat for round wins in current game
        incrementPlayerStat(2, 0, 1)  # increment the computer's stat for round loss in current game

def continuePlaying():
    answer = input("would you like to keep playing y/n?\n")
    while not ( answer.lower() == 'y' or answer.lower() == 'n'):
        answer = input("Error: please use y/n to answer. Would you like to keep playing?\n")
    if answer == 'y':
        return True
    return False

def gameWinner():
    if (getStat(0,0) + getStat(1,0)) > getStat(2,0): #if the sum of wins by the players is greater than the wins by computer. Computer is not the overall winner.
        if (getStat(0,0)) == (getStat(1,0)): # if their wins are equal, check who lost the least amount of times.
            if(getStat(0,1) < getStat(1,1)): # if player 1 lost the least amount of time player 1 has won the game
                incrementPlayerStat(0,3,0) # increment player 1 game wins in overallStats
                incrementPlayerStat(1,4,0) # increment play 2 game loss in overallStats
                print("Overall Winner is: " + player1Name + "!\n")
            elif(getStat(0,1) == getStat(1,1)): # if players loss are tied, then it's a tie
                incrementPlayerStat(0,5,0) # increment player 1 game wins in overallStats
                incrementPlayerStat(1,5,0) # increment play 2 game loss in overallStats
                print("Overall Winner is: TIE between humans!\n")
            else:
                incrementPlayerStat(1,3,0)
                incrementPlayerStat(0,4,0)
                print("Overall Winner is: " + player2Name + "!\n")
        if (getStat(0,0) > getStat(1,1)):
            incrementPlayerStat(0,3,0)
            incrementPlayerStat(1,4,0)
            print("Overall Winner is: " + player1Name + "!\n")
        else:
            incrementPlayerStat(1,3,0)
            incrementPlayerStat(0,4,0)
            print("Overall Winner is: " + player2Name + "!\n")
    if (getStat(0,0) + getStat(1,0)) == getStat(2,0):
        # there is a tie
        incrementPlayerStat(0,5,0)
        incrementPlayerStat(1,5,0)
        print("Overall Winner is: TIE!\n")
    else:
        incrementPlayerStat(0,4,0)
        incrementPlayerStat(1,4,0)
        print("Overall Winner is: Computer!\n")

def getWeaponFromChoice(weapon):
    if weapon == 1:
        return "Rock"
    elif weapon == 2:
        return "Paper"
    elif weapon == 3:
        return "Scissors"
    else:
        return "Saw"


if __name__ == '__main__':
    getNames()
    initializeStats()
    menu()

