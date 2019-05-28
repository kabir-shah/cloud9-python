from __future__ import print_function

"""Procedure (1-12)"""

slogan = 'My school is the best'

# 5 int, float, and long can represent the number 6 million

# 6 The second input produces an error because the "+" operator doesn't accept
# different types of inputs, and the inputs given were a string and an integer.
# In the first example, both were strings, even though different quotes were
# used.

# 7 An index n accesses the (n+1)th character of the string because the first
# character corresponds to the index of 0. When the index is 26, it attempts
# to access the 27th character, which doesn't exist. Negative indexes start at
# the last character, and go back from the end. -1 corresponds to the last
# character, -2 corresponds to the second to last, and so on. slogan[-7] returns
# "h" because it is the 7th to last character.

# 8 Slicing
print(slogan[17:21])

# 9 Slicing & Concatenation
print(slogan[:13] + "DHS, and it " + slogan[10:] + "!")

# 10
activity = 'theater'
len(activity) # -> 7

# 10a Explain
# The word "theater" has seven letters, so the length is 7.

activity[0 : len(activity)-1]

# 10b Explain
# This slices from the first character *until* the last index, which is found
# by the length minus one because indexes start at zero. This means that the
# slice contains everything except the last character, "theate"

# 11 Explain
'test goo' in 'Greatest good for the greatest number!' # -> True

# The code returns true because the string contains the text
# 'Greatest good for the greatest number!'
#      ^^^^^^^^

# 12 How Eligible Function

def how_eligible(essay):
    """
    Returns 0-4 based on how many requirement characters are within the essay
    """
    
    score = 0
    
    for char in ["?", "\"", ",", "!"]:
        if char in essay:
            score += 1
            
    return score
    
def how_eligible_one_line(essay):
    return sum([1 if char in essay else 0 for char in ["?", "\"", ",", "!"]])

#1.3.5 Function Test

print(how_eligible('This? "Yes." No, not really!')) # -> 4
print(how_eligible('Really, not a compound sentence.')) # -> 2

# Yes. I believe I did it correctly.