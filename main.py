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

# name is unique if and only if, the names are not the same regardless of capitalization
def UniqueName(p1name, p2name):
    return p1name.lower() != p2name.lower()

# a name is valid when the name's character length is more than the minimum and less than the maximum
# while also being unique
def validateName(p1name, p2name):
    return (len(p1name) > MINSIZE and len(p1name) < MAXSIZE) and UniqueName(p1name, p2name)


# get player 1's name, throw an error if name is not valid
while not validateName(player1Name, player2Name):
    player1Name = input("What is the name of the first player?")
    if not validateName(player1Name, player2Name):
        print(f"ERROR: the name entered for player 1 is not valid, name must be more than "  + str(MINSIZE) + " and " +
                "less than " + str(MAXSIZE) + " characters.")

# get player 2's name, throw an error if not valid. NOTE: in the error message we call player 1 by their given name
while not validateName(player2Name, player1Name):
    player2Name = input("what is the name of the second player?")
    if not validateName(player2Name, player1Name):
        print(f"ERROR: the name entered for player 2 is not valid, name must be more than "  + str(MINSIZE) + " and " +
                "less than " + str(MAXSIZE) + " characters AND must be unique compared to " + player1Name + "'s name.")

