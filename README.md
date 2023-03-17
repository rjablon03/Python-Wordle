# Python-Wordle
A version of Wordle that runs in the terminal. I'm new to Python so this is at a beginner level.

The program randomly selects a 5 letter word from a list called words. That randomly selected word is held in the answer variable.
Then, the user types in a 5 letter guess (if the user input is not 5 characters long, the user has to re-enter a word).
Next, the program compares the user input to the answer and outputs the users guess like so...

b !!!
r !
a !
i
n

Three exclamation marks means that the letter is not in the answer, and 1 exclamation mark means that the letter is in the answer,
however the user put that letter in the wrong position. If there is nothing next to the letter, the letter is in the correct position.

Currently, I don't have a way of checking to see if the user input is a word. If there are any other considerations I should think about
or if you have any other suggestions, let me know!
