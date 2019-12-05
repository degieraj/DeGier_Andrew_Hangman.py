import os
from random import randint

# FUNCTION DEFINITIONS

# Function to import words from text file and read into a list
def read_words():
	fp = open('word_list.txt','r')
	fp.seek(0)
	wordlist = fp.read().splitlines()
	fp.close
	return wordlist

# Function to randomly select a word at random from the imported list
def game_word(wordlist):
	gameword = wordlist[randint(0,len(wordlist)-1)]
	return gameword

# Function compares the guessed letters and the gameword and creates a string with * over unguessed letters
def blanked_letters(guesses,gameword):
	word_reveal = ''
	for char in gameword:
		if char in guesses:
			word_reveal = word_reveal+char
		else:
			a = '*'
			word_reveal = word_reveal+a
	return word_reveal

# Clear the screen (windows) to make the game clearer
clear = lambda: os.system('cls')
clear()

# Read in word list and select a word at random
gameword = game_word(read_words())
print(gameword)

print("\nLet's play Hangman!\n")

# Set up the game variables
guesses = ''
incorrect = 0
reveal = blanked_letters(guesses,gameword)

# Loop until 
while incorrect < 7:

	# Loop until player has guessed all letters in the the gameword correctly
	if reveal != gameword:

		# Tidy up the plural tries/try
		if 7 - incorrect == 1:
			plural = 'try'
		else:
			plural = 'tries'

		# Printout of current game status
		letter = input(f'{7 - incorrect} {plural} left  {reveal}  Please enter your next guess: ')
		
		# Loop to see if the guessed letter is correct, incorrect or has been guessed before
		if letter in guesses:
			print("You've already tried that letter")
		else:
			if letter in gameword:
				print('Correct guess')
				guesses = guesses + letter
				reveal = blanked_letters(guesses,gameword)
			else:
				print("That's an incorrect guess")
				incorrect += 1
				guesses = guesses + letter
	else:
		print('Congratulations you win')
		break

# Final you lose statement if all guesses used up
if incorrect == 7:
	print('You lose')
else:
	exit()

