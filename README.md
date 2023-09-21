# files_write_read
This is set of two programs written to learn how to manipulate files. 

The file play.py plays the rock-paper-scissors (rps) game with the user. The computer decides one of the three options randomly and the user types in their input on the keyboard. While doing so, the program records the choices made by the user (i.e. rock, paper or scissors) on to a file named responses.txt. (The exact path may depend on the local computer so pls change it)

The file replay.py reads the users' responses from the same file above (responses.txt) and it plays the game again with the computer deciding from a random choice. While playing the game, it mantains a record of who is winning (computer, user or tie). Finally it provides a summary of the number of times computer won, user won and it tied. As the number of times the game is played increases (upwards of 100, 1000, 10k, 100k etc), the number of wins should be closer to 33.33% for each of the option. Since the number of times this game is played is not so large, you often see skewed results. 
