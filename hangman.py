done = False
import random
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p"
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
"""
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
"""

# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


# Feel free to use this list of ascii art for your game --- thanks for this
word_list = ["CARROT"]
guessed_letters = []
misses = 0
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = word_list[random.randrange(len(word_list))]

while not done:
    current_letter = input("What letter do you guess?").upper()
    if current_letter.lower() in alphabet:
        guessed_letters.append(current_letter.upper())
        if current_letter in word:
            print(HANGMANPICS[misses])
    else:
        print("That's not a letter.")

    game_over = False
    while game_over:
        keep_going = input("Do you want to play again?    (y/n)")
        if keep_going == "y":
            game_over = True
            print("\n\n\n\n\n\nTIME FOR SOME HANGMAN")
        if keep_going == "n":
            done = True
            game_over = False



