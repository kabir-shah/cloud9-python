"""Part 1: Tuples, Syntax"""

# 5 My teacher requires snake_case for Python variable names, and has
# a convention for multi line comments being headers of the directions.

# 6 Tuples
some_values = ('a', 'b', 3)

# 6a The following line will result in 'b', because it is the second element
# of the tuple, and the "1" index will access it because indexes start at 0.
some_values[1]

# 6b the following line will return the tuple ('a', 'b'), because it slices
# from the first value until the last one, giving the first two elements.
some_values[0:2]

a = 10
b = (9, a, 11)
a = 15

# 7a The following will result in True, because b's second value was bound to
# the data in a, which was 10 at the time. Even if a changed, b's second value
# will still be 10, making this equality true
b[1] == 10

b = (9, a , 11)

# 7b The following will result in 15, because b was reassigned, and the second
# value will now be assigned using a's new value of 15.
b[1]

"""Part 2: Lists"""

values = ['a', 'b', 3]

# 8 This will result ['b', 3], because it slices from the second element to the
# end of the list inclusively, making it every element except the first.
values[1:]

values[2] = '3'

# 9 This will result in False, because the third value was changed to a string
# on the previous line.
values[2] == 3

values = values + [4, 5]

# 10a This will result in ['a', 'b', '3', 4, 5], because every element in the
# second list was appended to the first.
values

values.append([6, 7])

# 10b This will result in ['a', 'b', '3', 4, 5, [6, 7]], because the list [6, 7]
# was appended to the end of the list, making a list inside of a list.
values

# 11
# values = values + 5 results in an error because the "+" operator only accepts
# two arguments of the same type, and in this case the types are list and int.

a = 6
a *= 3

# 12 The following results in 18, because a was assigned to itself multiplied by
# 3.
a

"""Part 3: Lists and the random module"""

# 14 Roll two dice
import random

def roll_two_dice():
	return random.randint(1, 6) + random.randint(1, 6)

"""Conclusion"""
a = 'abcde'
b = ('a', 'b', 'c', 'd', 'e')
c = ['a', 'b', 'c', 'd', 'e']

# 1 The values a, b, and c are different data types. a is a string, and is used
# to represent only series of characters, while the other two can represent any
# set of types. b's tuple is immutable (b is mutable still), and the values
# inside the tuple cannot be changed. c is mutable, and can be changed to
# add, replace, or remove any values.

# 2 Computer programming languages have a variety of variables types to create
# abstraction to allow for higher level programming. Everything *can* be
# represented as an infinite length integer, and that is how the computer itself
# implements datatypes, but Python implements abstractions over this to allow
# for different common use cases and data structures to be modeled easily.
 
# 3 Strings, tuples, and lists are ways to store collections of data. Strings
# can only store sets of characters, but are mutable. Tuples can store any
# amount of any data type, but are immutable. Lists can store any amount of any
# data type, and are mutable to allow for changing the list.

"""Assignment Check"""

#1.3.6 Function Test
print(roll_two_dice())