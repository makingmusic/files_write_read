# all common functions

STORAGE_FILE = "/Users/makingmusic/Desktop/code/files_write_read/responses.txt"

# initial variables
responseStrings = ["rock", "paper", "scissors"]

def whoWins(p, c):
    if p == c:
        return 0 # tie
    elif p == 0 and c == 1:
        return 2 # computer
    elif p == 0 and c == 2:
        return 1 # player
    elif p == 1 and c == 0:
        return 1 # player
    elif p == 1 and c == 2:
        return 2 # computer
    elif p == 2 and c == 0:
        return 2 # computer
    elif p == 2 and c == 1:
        return 1 # player
    else:
        return -1 # invalid choice


