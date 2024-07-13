# Master Mind Game and Solver

Rules for the game can be found [here](<https://en.wikipedia.org/wiki/Mastermind_(board_game)>). The code in `main.py` is for 6 colors and 4 pegs but can be changed to use other amount of colors.

# How to play

To begin, run the file in the terminal: `python3 main.py`. Once the game begins, you should take the first guess.

To guess, write the first letter of the color you would like to guess. In the current game, there are six colors: red (r), blue (b), yellow (y), green (g), orange (o), and purple (p). A guess consist of four colors, which could be repeated, separated by a space. Examples: `r b g y`, `r r b o`, `p p p p`, etc.

After the first guess, you will get a message with the amount of black key pegs and white key pegs in no specific order. A black key peg means that you got a color in the correct position and a white key peg means that you have a correct color but in the wrong position. This will be given as four strings `b`, `w`, and `_` for black key peg, white key peg, and not a black key peg nor a white key peg, respectively.

This will continue until you get the correct combination, or you have used all your guesses.

# Using the Five-guess algorithm

The [Five-guess algorithm](<https://en.wikipedia.org/wiki/Mastermind_(board_game)#Worst_case:_Five-guess_algorithm>) will be implemented soon.
