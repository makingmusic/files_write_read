import random
from common_functions import * # import all functions from common_functions.py

numTimesComputerWon = 0
numTimesPlayerWon = 0
numTimesTie = 0
numTimesPlayed = 0

fr = open("/Users/makingmusic/Desktop/code/files_write_read/responses.txt", "r")
responses = fr.readlines()
fr.close()

for i in range(len(responses)):
    responses[i] = responses[i].strip()

for response in responses:
    computerChoice = random.randrange(0, 3) # 0 = rock, 1 = paper, 2 = scissors
    playerChoiceStr = response
    computerChoiceStr = responseStrings[computerChoice]
    playerChoice = responseStrings.index(playerChoiceStr)
    
    numTimesPlayed += 1
    whoWon = whoWins(playerChoice, computerChoice)
    if (whoWon == -1):
        print("Something went wrong. p = ", playerChoice, " c = ", computerChoice)
    
    if (whoWon == 0):
        numTimesTie += 1
    elif (whoWon == 1):
        numTimesPlayerWon += 1
    elif (whoWon == 2):
        numTimesComputerWon += 1

ratioPlayerWin = round(numTimesPlayerWon / numTimesPlayed, 4)
ratioComputerWin = round(numTimesComputerWon / numTimesPlayed, 4)
ratioTie = round(numTimesTie / numTimesPlayed, 4)

print ("Played " + str(numTimesPlayed) + " times.")
print ("Player  : " + str(ratioPlayerWin))
print ("Computer: " + str(ratioComputerWin))
print ("Tie     : " + str(ratioTie))

