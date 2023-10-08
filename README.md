# files_write_read
This is set of two programs written to learn how to manipulate files. 

The file play.py plays the rock-paper-scissors (rps) game with the user. The computer decides one of the three options randomly and the user types in their input on the keyboard. While doing so, the program records the choices made by the user (i.e. rock, paper or scissors) on to a file named responses.txt. (The exact path may depend on the local computer so pls change it)

The file replay.py reads the users' responses from the same file above (responses.txt) and it plays the game again with the computer deciding from a random choice. While playing the game, it mantains a record of who is winning (computer, user or tie). Finally it provides a summary of the number of times computer won, user won and it tied. As the number of times the game is played increases (upwards of 100, 1000, 10k, 100k etc), the number of wins should be closer to 33.33% for each of the option. Since the number of times this game is played is not so large, you often see skewed results. 

GitHub Copilot: [Markdown]

# Rock Paper Scissors Analyzer

This program analyzes the results of the past games of rock paper scissors and shares the final statistics of the games played so far.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Run the program using `python replay.py`

## Usage

The program reads the past game results from a file named `responses.txt` located in the `files_write_read` directory. The file should contain one game result per line, with the player's move followed by the computer's move, separated by a comma.

Example:

```
rock,paper
scissors,scissors
paper,rock
```

The program will then analyze the results and print the final statistics of the games played so far.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request to suggest changes or improvements.

