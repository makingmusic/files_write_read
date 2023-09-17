# rock paper scissors game
import random
from common_functions import * # import all functions from common_functions.py

# establish choices
computerChoice = random.randrange(0, 3) # 0 = rock, 1 = paper, 2 = scissors
playerChoiceStr = input("(r)ock, (p)aper, or (s)cissors? ")

# convert player choice to number
if playerChoiceStr == "r":
    playerChoice = 0 # rock
elif playerChoiceStr == "p":
    playerChoice = 1 # paper
elif playerChoiceStr == "s":
    playerChoice = 2 # scissors 

# print choices
print("You chose " + responseStrings[playerChoice])
print ("The computer chose " + responseStrings[computerChoice])

# determine winner
whoWon = whoWins(playerChoice, computerChoice)
if (whoWon == -1):
    print("Something went wrong. p = ", playerChoice, " c = ", computerChoice)

if (whoWon == 0):
    print("Tie!")
elif (whoWon == 1):
    print("Player wins!")
elif (whoWon == 2):
    print("Computer wins!")

# write the response to a file
fa = open (STORAGE_FILE, "a")
fa.write(responseStrings[playerChoice] + "\n")
fa.close()

