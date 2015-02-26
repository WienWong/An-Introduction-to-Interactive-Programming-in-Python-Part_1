
# Ex1 for logic and conditionals

###################################################
# 1. Write a Python function is_even that takes as input the parameter number (an integer) and returns True if number is even
# and False if number is odd. Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.

# Compute whether an integer is even.

###################################################
# Is even formula
# Student should enter function on the next lines.

def is_even(number):
    if number%2==0:
        return True
    elif number%2==1:
        return False
    
# Solution:
def is_even(number):
    """Returns whether the number is even."""
    return (number % 2) == 0

###################################################
# Tests
# Student should not change this code.

def test(number):
    """Tests the is_even function."""
    if is_even(number):
        print number, "is even."
    else:
        print number, "is odd."

test(8)
test(3)
test(12)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#8 is even.
#3 is odd.
#12 is even.

###################################################
# 2. Write a Python function is_cool that takes as input the string name and returns True if name is either "Joe", "John" or
# "Stephen" and returns False otherwise. (Let's see if Scott manages to catch this?)

# Compute whether a person is cool.

###################################################
# Is cool formula
# Student should enter function on the next lines.

def is_cool(name):
    return (name=="Joe") or (name=="John") or (name=="Stephen") 

###################################################
# Tests
# Student should not change this code.

def test(name):
    """Tests the is_even function."""
    
    if is_cool(name):
        print name, "is cool."
    else:
        print name, "is not cool."

test("Joe")
test("John")
test("Stephen")
test("Scott")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.

###################################################
# 3. Write a Python function is_lunchtime that takes as input the parameters hour (an integer in the range [1,12]) and is_am 
# (a Boolean “flag” that represents whether the hour is before noon). The function returns True when the input corresponds
# to 11am or 12pm (noon) and False otherwise. 

# Compute whether the given time is lunchtime.

###################################################
# Is lunchtime formula
# Student should enter function on the next lines.

def is_lunchtime(hour, is_am):
    return (hour==11 and is_am) or (hour==12 and is_am)

###################################################
# Tests
# Student should not change this code.

def test(hour, is_am):
    """Tests the is_lunchtime function."""
    print hour,
    if is_am:
        print "AM",
    else:
        print "PM",
    if is_lunchtime(hour, is_am):
        print "is lunchtime."
    else:
        print "is not lunchtime."

test(11, True)
test(12, True)
test(11, False)
test(12, False)
test(10, False)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#11 AM is lunchtime.
#12 AM is not lunchtime.
#11 PM is not lunchtime.
#12 PM is lunchtime.
#10 PM is not lunchtime.

###################################################
# 4. Write a Python function is_leap_year that take as input the parameter year and returns True if year (an integer) is a 
# leap year according to the Gregorian calendar and False otherwise. 

# Compute whether the given year is a leap year.

#
#if (year is not divisible by 4) then (it is a common year)
#else
#if (year is not divisible by 100) then (it is a leap year)
#else
#if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)
#

###################################################
# Is leapyear formula
# Student should enter function on the next lines.

def is_leap_year(year):
    if (year%4 != 0):
        return False
    else:
        if (year%100 != 0):
            return True
        else:
            if (year%400 != 0):
                return False
            else:
                return True
                
# Solution:
def is_leap_year(year):
	"""
	Returns whether the given Gregorian year is a leap year.
	"""	
	return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))
	
###################################################
# Tests
# Student should not change this code.

def test(year):
    """Tests the is_leapyear function."""
    if is_leap_year(year):
        print year, "is a leap year."
    else:
        print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2013)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.

###################################################
# 5. Write a Python function interval_intersect that takes parameters a, b, c, and d and returns True if the intervals [a,b] 
# and [c,d] intersect and False otherwise. While this test may seem tricky, the solution is actually very simple.

# Compute whether two intervals intersect.

###################################################
# Interval intersection formula
# Student should enter function on the next lines.

# Solution:
def interval_intersect(a, b, c, d):
    """Returns whether the intervals [a,b] and [c,d] intersect."""
    return (c <= b) and (a <= d)

###################################################
# Tests
# Student should not change this code.

def test(a, b, c, d):
    """Tests the interval_intersect function."""
    print "Intervals [" + str(a) + ", " + str(b) + "] and [" + str(c) + ", " + str(d) + "]",
    if interval_intersect(a, b, c, d):
        print "intersect."
    else:
        print "do not intersect."

test(0, 1, 1, 5)
test(1, 2, 0, 1)
test(0, 1, 2, 3)
test(2, 3, -8, 1)
test(0, 3, 1, 2)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Intervals [0, 1] and [1, 5] intersect.
#Intervals [1, 2] and [0, 1] intersect.
#Intervals [0, 1] and [2, 3] do not intersect.
#Intervals [2, 3] and [-8, 1] do not intersect.
#Intervals [0, 3] and [1, 2] intersect.



