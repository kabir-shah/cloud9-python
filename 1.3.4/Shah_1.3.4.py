from __future__ import print_function

'''Part 1: Nested "if" structures and testing'''

# 1 Food ID
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
# 1a The food ID of "apple" returns from line 17.

# 1b
# "orange" will result in line 15 being run
# "apple" will result in line 17 being run
# "potato" will result in line 20 being run
# "pizza" will result in line 22 being run

# 1c Line 20 will never result in "banana" being reported as starchy because it
# is considered a fruit. Since fruits are checked for first, the banana will be
# reported as a fruit instead of starchy.

# 2 Food ID Test
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()'
    if food_id("potato") != "Starchy, NOT Fruit":
        works = "potato bug in food_id()" 
    if food_id("pizza") != "NOT Starchy, NOT Fruit":
        works = "pizza bug in food_id()"
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

# 3 Flow Chart Function
def f(n):
    '''Report information about a given integer'''
    if type(n) is int:
        if n % 2 == 0:
            if n % 3 == 0:
                return "%d is a multiple of six" % n
            else:
                return "%d is even" % n
        else:
            return "%d is odd" % n
    else:
        return str(n) + " is not an integer"
        
# 4 Test cases: Test cases should include a non-integer value, an odd number,
# an even number, and a multiple of six

# 5 Test Suite
def f_test():
    '''Unit test for f(n), returns True if working and a bug report if not'''
    works = True 
    
    if f("string") != "string is not an integer":
        works = "bug in non-integer report"
    if f(1) != "1 is odd":
        works = "bug in odd integer report"
    if f(2) != "2 is even":
        works = "bug in even integer report"
    if f(6) != "6 is a multiple of six":
        works = "bug in multiple of six report"
    
    return works
    
'''Part 2: The raw_input() function, type casting, and print() from Python 3'''

# 8 Guess Once Function
import random

# 8a: Explanation of line 11
# Prints the number and the guess with a space in between each (the default
# separator). It will end with an exclamation mark followed by a new line.

# 8b: Modification of guess_once()
def guess_once():
    '''
    Take a guess number and give feedback to how close it was to a secret
    number
    '''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess < secret:
        print('Too low - my number was ', secret, '!', sep='')
    elif guess > secret:
        print('Too high - my number was ', secret, '!', sep='')
    else:
        print('Right, my number is', guess, end='!\n')
        
# 9 Quiz Decimal
def quiz_decimal(low, high):
    '''Asks for a number and verifies it is between low and high'''
    guess = float(raw_input("Type a number between %f and %f: " % (low, high)))
    if guess <= low:
        print("No, %f is less than %f" % (guess, low))
    elif guess >= high:
        print("No, %f is greater than %f" % (guess, high))
    else:
        print("Good! %f < %f < %f" % (low, guess, high))
        
'''Conclusion'''

# 1 Glass box testing must test each branch created in functions using if
# structures.

# 2 In any given if-else structure, only one block will execute. Any nested
# structures within these blocks will test and only run one block.

# 3 Test suites verify that a program works as expected by testing edge cases
# and all critical paths created by branches. Programmers may write test suites
# first to write their programs while constantly testing and accounting for
# different test cases.

# 4 Yes.

def is_int(n):
    return type(n) is int

def is_even(n):
    return n % 2 == 0
    
def is_multiple_of_six(n):
    return n % 6 == 0
    
def f_challenge(n):
    if not is_int(n):
        return "%s is not an integer" % str(n)
        
    elif is_multiple_of_six(n):
        return "%d is a multiple of six" % n
    
    elif is_even(n):
        return "%d is even" % n
        
    else:
        return "%d is odd" % n
        
def f_challenge2(n):
    c = lambda x:("%x"%x).decode("hex");
    
    if type(n) is not int:
        return c(213800067694141039994394574200666499931745772914L) % str(n)
    
    elif n%6==0:
        return c(3581357750231870966530291571888148621078339901461850488L) % n
    
    elif n&1==0:
        return c(176574569798012574786926L) % n
        
    else:
        return c(689744413273487271012L) % n

def f_challenge3(n):
    exec("6966206e6f742069735f696e74286e293a0a2020202072657475726e20222573206973206e6f7420616e20696e746567657222202520737472286e290a656c69662069735f6d756c7469706c655f6f665f736978286e293a0a2020202072657475726e202225642069732061206d756c7469706c65206f6620736978222025206e0a656c69662069735f6576656e286e293a0a2020202072657475726e20222564206973206576656e222025206e0a656c73653a0a2020202072657475726e20222564206973206f6464222025206e".decode("hex"))

def encode2(x):
    for byte in list(bytearray(x)):
        print ("{0:08b}".format(byte), end="")
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
print(f_challenge(1.1))
print(f_challenge(2))
print(f_challenge(3))
print(f_challenge(6))