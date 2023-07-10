import random

# Code for a Master Mind Game
# 
# Rules: https://en.wikipedia.org/wiki/Mastermind_(board_game)
# 
# Version of this game: 6 colors and 4 spots
# 
# colors_meaning = {
#     "r" : "red",
#     "b" : "blue",
#     "y" : "yellow",
#     "g" : "green",
#     "o" : "orange",
#     "p" : "purple",
# }

############
### GAME ###
############

class Game:
    def __init__(self):
        """
        Create variables the game will use in each timestep
        """
        self.length = 4
        self.code_colors = ["r", "b", "y", "g", "o", "p"]
        self.board = list(random.sample(self.code_colors, self.length))
        self.guesses = []
        self.num_guesses = 0
        self.max_guesses = 8
        self.state = "ongoing"
        self.code_colors_amount = {color:0 for color in self.code_colors}
        for color in self.board:
            self.code_colors_amount[color] += 1
        
    def timestep(self):
        """
        Every timestep is a guess, there are a maximum of self.max_guesses
        """
        if self.state == "ongoing":
            # Let the user take a guess
            if self.num_guesses == 0:
                guess = input('Enter four colors, separated by spaces, for your guess using the following abbreviations - r, b, y, g, o, p\n\nGuess: ')
            else:
                guess = input('Take another guess\n\nGuess: ')
            guess = guess.strip()
            guess = guess.split(" ")

            # Check if the guess is correct
            if self.board == guess:
                self.state = "won"
                return f"\nYou {self.state}!!!\n"

            # Check the guess is in the correct form
            for color in guess:
                if color not in self.code_colors:
                    print('\nRemember to enter a the colors separated by commas using the following abbreviations - r, b, y, g, o, p\n')
                    return self.timestep()

            # Return how many were correct, in the wrong place, or completely wrong
            self.num_guesses += 1
            self.guesses.append(guess)

            # Create a guess color amount dict
            guess_colors_amount = {color:0 for color in self.code_colors}
            for color in guess:
                guess_colors_amount[color] += 1

            # Check for misplaced
            misplaced = 0
            for color in guess_colors_amount:
                misplaced += min(guess_colors_amount[color], self.code_colors_amount[color])

            # Check for correct
            correct = 0
            for i in range(len(guess)):
                guess_color = guess[i]
                board_color = self.board[i]
                if guess_color == board_color:
                    correct += 1
                    misplaced -= 1  # Remove 1 since it will be overcounting
            
            # Return a list of how many were correct, mispaced, and wrong
            wrong = self.length - (correct + misplaced)
            correct_misplaced = []
            if correct != 0:
                for i in range(correct):
                    correct_misplaced.append("b")
            if misplaced != 0:
                for i in range(misplaced):
                    correct_misplaced.append("w")
            if wrong != 0:
                for i in range(wrong):
                    correct_misplaced.append("_")

            # Return feedback 
            print(f"\nThe result of this round, in no particular order: {correct_misplaced}\n\n\n")

            # Make sure the game is still ongoing
            if self.num_guesses == self.max_guesses:
                self.state = "lost"
                return f"\nYou {self.state} and the code was {self.board}\n\n"

            return self.timestep()


# Play game without solver
print(Game().timestep())


##############
### SOLVER ###
##############

# Implement the solver (Five-guess algorithm)





