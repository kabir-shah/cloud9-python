from __future__ import print_function
import random
import time

hangmen = None
phrases = None
special_characters = [" ", ".", ",", "\"", "'", "!", "?"]

# Process the hangmen ascii characters and split them up into a list
with open("Hangman/hangmen.txt", "r") as hengmen_file:
	hangmen = hengmen_file.read().split("\n\n")
	
# Process the phrases and convert them into a list with all lowercase phrases
# for simplicity.
with open("Hangman/phrases.txt", "r") as phrases_file:
	phrases = map(lambda string: string.lower(), phrases_file.read().split("\n"))
	
class color:
	"""
	Terminal color codes for printing in various different colors.
	"""

	blue = "\033[94m"
	yellow = "\033[93m"
	green = "\033[92m"
	red = "\033[91m"
	end = "\033[0m"
	black  = "\033[30m"


def hangman_display(guessed, secret):
	"""
	Returns the string the hangman player would see. If a letter of the secret 
	word is correctly guessed, that letter will be shown to the user. If the 
	letter is not guessed, a dash will be returned instead.
	
	Takes a string of guessed letters and a secret, and returns a formatted
	secret with unguessed letters hidden.
	"""
	text = ""
	
	for char in secret:
		if char in special_characters:
			text += char
		elif char in guessed:
			text += char
		else:
			text += "-"
		
	return text
	
def hangman():
	"""
	Begins a hangman game that randomly picks a secret and constantly requests
	an input letter until the secret is guessed or ten guesses are used.
	"""
	
	# Pick a secret, and initialize the guessed letters and number of guesses
	secret = random.choice(phrases)
	guessed = ""
	guesses = 0
	
	# Get the hangman display with guessed letters of the secret showing
	display = hangman_display(guessed, secret)
	
	# Continue requesting input until there are no guesses remaining or the guess
	# matches the secret.
	while guesses < 7 and display != secret:
		print("\n")
		print(hangmen[guesses])
		print(color.blue + display + color.end)
		print(color.yellow + "Guessed: " + color.end + (", ".join(guessed) or "None"))
		print(color.yellow + "Guesses Remaining: " + color.end + str(7 - guesses))
		guess = raw_input(color.green + "> " + color.end).lower()
		
		# Give a hint with an unused random character from the secret, and
		# use a guess.
		if guess == "hint":
			hint = random.choice(secret)
			while hint in guessed or hint in special_characters:
				hint = random.choice(secret)
			print(
				color.blue + "hint: " + color.end + "Try the letter \"" + hint + "\""
			)
			guesses += 1
			continue
		# Developer cheat: print out the secret
		elif guess == "cheat":
			print(color.blue + "cheat activated: " + color.end + secret)
			continue
		
		for guessChar in guess:
			# See if already guessed
			if guessChar in guessed:
				print(
					color.blue + "note: " + color.end + "You already guessed \"" +
					guessChar + "\""
				)
				
			else:
				guessed += guessChar
				
				# Use a guess if the guess is wrong
				if guessChar not in secret:
					guesses += 1
				
					if guesses >= 7:
						break
				
		# Generate a new display for every turn
		display = hangman_display(guessed, secret)
		
	print(color.blue + display + color.end)
	
	# Print the winning or losing states
	if secret == display:
		print(color.green + "You win!" + color.end)		
	else:
		print(color.red + "You lose" + color.end)
		
	if raw_input(color.yellow + "Play again?" + color.end + " (y/n): ").lower() == "y":
		print("\n")
		hangman()

# Print instructions and begin game
print(
    color.green + "\n---> Spongebob Hangman Game <---" + color.end +
    "\nBy: Josh and Kabir"
)
time.sleep(1)

print(color.blue + """
Are you ready, kids?
I said, are you ready?
Who lives in a pineapple under the sea?
Spongebob Squarepants
Absorbent and yellow and porous is he
Spongebob Squarepants
If nautical nonsense be something you wish
Spongebob Squarepants
Then drop on the deck and flop like a fish
Spongebob Squarepants
Spongebob Squarepants
Spongebob Squarepants
Spongebob Squarepants
Spongebob Squarepants
""" + color.end)
time.sleep(1)

print("Type 'hint' for a helpful tip, or 'cheat' for a REALLY helpful tip.")
print("Guess the Spongebob Phrase!")
time.sleep(1)

hangman()