# Andrew De Gier Module 3 Assessment
'''
This script runs a text based hangman game utilising a premade
word dictionary contained in a seperate word file
'''

import os
from random import randint

# FUNCTION DEFINITIONS

def read_words():
    '''Reads in a list of words from a text file'''
    text_file = open('word_list.txt', 'r')
    # Set the cursor to the start of the text file
    text_file.seek(0)
    # Read in each line as an element
    wordlist = text_file.read().splitlines()
    return wordlist

def game_word(word_list):
    '''Randomly selects a word from the imported list to be guessed by the user'''
    selected_word = word_list[randint(0, len(word_list)-1)]
    return selected_word

def blanked_letters(guessed_letters, word):
    '''Compares the guessed letters and the gameword and creates a string
    with * replacing unguessed letters'''
    word_reveal = ''
    for char in word:
        if char in guessed_letters:
            word_reveal = word_reveal+char
        else:
            hidden_letter = '*'
            word_reveal = word_reveal+hidden_letter
    return word_reveal

def status_printout(wrong_guesses, plural_word, guessed_letters, word_reveal):
    '''Prints out the current game status and returns the user's next guess'''
    line = input(f'\n{7 - wrong_guesses} {plural_word} left    '
                 f'Previous entries: {guessed_letters}\n'
                 f'{word_reveal}    Please enter your next guess: ')
    return line.lower()

def input_valid(user_input):
    '''Checks if a user's input is valid i.e. is a single letter of the alphabet'''
    if len(user_input) == 1 and user_input.lower().isalpha():
        return True
    print("You must enter a single letter of the alphabet")
    return None

def main():
    '''Main program'''

    # Clear the screen (windows) to make the game clearer
    clear = lambda: os.system('cls')
    clear()

    # Read in word list and select a word at random
    gameword = game_word(read_words())

    print("\nLet's play Hangman!")

    # Set up the game variables
    guesses = ''
    incorrect = 0
    reveal = blanked_letters(guesses, gameword)

    # Loop until player uses up all their lives
    while incorrect < 7:

        # Loop until player has guessed all letters in the the gameword correctly
        if reveal != gameword:

            # Decide if it should be lives or life
            if 7 - incorrect == 1:
                plural = 'life'
            else:
                plural = 'lives'

            valid_entry = False
            while not valid_entry:
                # Printout of current game status
                letter = status_printout(incorrect, plural, guesses, reveal)
                valid_entry = input_valid(letter)

            # Loop to see if the guessed letter is correct, incorrect or has been guessed before
            if letter in guesses:
                print("You've already tried that letter")
            else:
                if letter in gameword:
                    print('Correct guess')
                    guesses = guesses + letter
                    reveal = blanked_letters(guesses, gameword)
                else:
                    print("That's an incorrect guess")
                    incorrect += 1
                    guesses = guesses + letter
        else:
            # If word guessed correclt print a win statement and clear the screen
            print(f'\nThe word was: {gameword}   You used {incorrect}/7 lives to guess correctly')
            input('Congratulations you win')
            clear()
            break

    # If all guesses used up print a lose statement and clear the screen
    if incorrect == 7:
        print(f'\nThe word was: {gameword}.')
        input('You lose')
        clear()

main()
