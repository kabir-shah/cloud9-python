from __future__ import print_function

'''Procedure'''

a = 3

# 1-5 N/A

'''Part 1: Conditionals'''

# 6a Prediction
assert((a**2 >= 9 and not a>3) == True)

# 6b Prediction
assert((a+2 == 5 or a-1 != 3) == True)

# 7 Condition
x, y = (90, 115)
assert(40 < x and x < 130 and 100 <= y and y <= 120)

'''Part 2: if-else Structures & the print() Function!!!'''

def age_limit_output(age):
    '''9a if-else example'''
    AGE_LIMIT = 13
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
    
# 9a Predictions

# I think that age_limit_output(10) will print that it is below the age limit
# because 10 is less than 13 (the age limit)

# I think that age_limit_output(16) will print that it is old enough because 16
# is greater than 13.

# 9b Report Grade Function
def report_grade(percent):
    '''Prints mastery level based on grade percent'''
    if percent >= 80:
        print(
            "A grade of %d indicates mastery.\nKeep up the good work!"
            % percent
        )
    else:
        print("A grade of %d does not indicate mastery." % percent)
        
# 10a Prediction: True because 3 is an integer and the list has the integer 3
# 10b Prediction: False because '3' is a string and the list does not have
# any strings

# 11 Letter in Word Function
def letter_in_word(guess, word):
    return guess in word
    
# 12 Hint Function
def hint(color, secret):
    print("The color %s %s in the secret sequence of colors." %
         (color, "IS" if color in secret else "IS NOT"))
         
'''Conclusion'''

# 1
# All blocks of code indented after if/else keywords are ran if a condition is
# met. If a condition is true, then the indented code after the "if" block is
# ran. If it is false, then the next "elif" conditions are checked until one is
# True and the indented code is ran. If nothing matches, then the code indented
# after the "else" block (if it exists) is ran.

# 2
# ==, >, <, >=, <=, and, not, or, in, and an extra one is "is". "is" checks if
# the type and value of two values are the same.

# 3

# Ira: Ira is right that the code will run no matter what, because it is in both
# branches. However, the program will not run slower by having it there twice,
# since only one will be evaluated, meaning that it will have the same
# performance as one print() call.

# Jayla: Jayla is right that the code will run no matter what, because it is in
# both branches. Jayla is also right that changing the code will require
# changing it in two places. Since the same print statement is used in both
# branches, a change would have to be applied in both places.

# Kendra: Kendra is right that the code will run no matter what, because it is
# in both branches. Kendra is partially right when she states that "the program
# will take up less memory if you wrote it just once". At run time, the program
# should take the same amount of memory as if the print statement were written
# once, since only one would get run. However, it will take up more memory since
# the file is larger, and as a result the Python bytecode will take up more
# memory.

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)

# I believe that I successfully completed the assignment because all functions
# behave as expected when running these tests.