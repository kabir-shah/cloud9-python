from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

"""Part 1: for loops, range(), and help()"""

# 4 Days Explanation
def days():
	"""
	Print out the first letter of each day of the week, and then print out the
	fifth through eight days of September.
	"""
	for day in 'MTWRFSS': 
		print(day + 'day')
	for day in range(5,8):
		print('It is the ' + str(day) + 'th of September')
        
# 6a Roll Hundred Pair
def roll_hundred_pair():
	"""Plots histogram of 100 of 2 six-sided dice rolls"""
	plt.hist([dice(2) for i in range(100)])	
	plt.savefig("1.3.7/roll_hundred_pair")
	
	
# 6b Dice roll
def dice(n):
	"""Returns sum of n six-sided dice rolls"""
	return sum([random.randint(1, 6) for i in range(n)])

"""Part 2: While loops"""

# 7 Explanation
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

# Line 35 is necessary because the loop needs to be executed at least once
# and the guess needs to be not in the answer for the while loop to execute.

# 8 Annotations
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
	'''
	Pick one winner from players, display them to the user, and
	ask them to guess until they get it right. Return how many
	guesses it took.
	'''
	winner = random.choice(players) 

	####
	# Print out each player in a comma-separated list
	# Could be written as ", ".join(players) but whatever
	####
	print('Guess which of these people won the lottery: ',end='')
	for p in players[:len(players)-1]: # Iterate *until* the last index (length - 1)
		print(p+', ', end='')
	print(players[len(players)-1]) # Print the last player (length - 1)
	
	####
	# Take input until it is the winner, and increment
	# the guesses until it is correct.
	####
	guesses = 1 
	while raw_input() != winner:
		print('Guess again!')
		guesses += 1
	print('You guessed in', guesses, 'guesses!')
    
	return guesses
    
# 9 Number guess
def goguess():
	"""
	Pick a number and constantly ask for a guess until it is correct, giving
	hints along the way.
	"""
	n = random.randint(1, 20)
	print("I have a number between 1 and 20 inclusive.")
	
	guesses = 0
	while True:
		guess = int(raw_input("Guess\n> "))
		guesses += 1
		
		if guess == n:
			print("Right! My number is " + str(n) + "! You guessed in " + str(guesses) + " guesses!")
			break
		else:
			print(str(guess) + " is too " + ("low" if guess < n else "high"))
			
# 10 It will take at most 5999 guesses, because you could pick n-1,
# and it will say that is is too high. Then you can guess n-2,
# which may also be too high. This can continue until you reach 1,
# giving the correct guess after 5999 guesses.
			
"""Part 3: Practice"""

# 11a Matches
def matches(tickets, winners):
	"""
	Return how many numbers are in common with the given lists
	"""
	return len(set(tickets) & set(winners))
	
# 11b Mastermind
def report(guess, secret):
	matched = 0
	rest_guess = set()
	rest_secret = set()
	
	for i in range(len(secret)):
		if secret[i] == guess[i]:
			matched += 1
		else:
			rest_guess.add(guess[i])
			rest_secret.add(secret[i])

	return [matched, len(rest_guess & rest_secret)]
	
"""Conclusion"""

# 1 The disadvantages of writing a program with unrolled loops
# is that it can become hard to keep track of and maintain.
# Also, it takes up more code to do something that could
# be done more efficiently with a loop. It is often harder
# to get an idea across when using unrolled loops than
# a normal loop where variables can be named to represent
# each part of something.

# 2 The relationship between iteration and analysis of data
# is that iteration is used to go through data and analyze
# each part of it.

# 3 A while loop repeats a given block of code while a condition
# is true. A for loop repeats a given block of code and provides
# an iteration variable for each element in an iterable.

# 4 My partner and I were able to discuss problems we had
# when implementing algorithms and find out new ways to
# solve them.

# 1.3.7 Function test

days()
roll_hundred_pair()
print("Roll 2 dice:", dice(2))
print("Roll 3 dice:", dice(3))
validate()
goguess()
print(matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17]))
print(report(['red','red','red','green','yellow'], ['red','red','yellow','yellow','black']))

# Yes, I believe I did it correctly as these were the examples provided.