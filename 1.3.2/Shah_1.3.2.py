def add_tip(total, tip_percent): 
    """Return the total amount including tip"""
    tip = tip_percent * total
    return total + tip
    
def hyp(leg1, leg2):
    """Returns length of hypotenuse given lengths of legs of a right triangle"""
    return (leg1 ** 2 + leg2 ** 2) ** 0.5
    
def mean(a, b, c):
    """Returns mean of three numbers"""
    return (a + b + c) / 3.0
    
def perimeter(base, height):
    """Returns perimeter of a rectangle given base length and height"""
    return (2.0 * base) + (2.0 * height)
    
# 1.3.2 Function Test
print add_tip(20, 0.15)
print add_tip(30, 0.15)
print hyp(3, 4)
print mean(3, 4, 7)
print perimeter(3, 4)