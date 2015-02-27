
# Ex 1 for logic and conditionals

# 6. Write a Python function name_and_age that take as input the parameters name (a string) and age (a number) and returns a 
# string of the form "% is % years old." where the percents are the string forms of name and age. The function should include 
# an error check for the case when age is less than zero. In this case, the function should return the string 
# "Error: Invalid age".

# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age(name, age):
    if age<0:
        return "Error: Invalid age"
    else:
        return name + " is " + str(age) + " years old."
    

###################################################
# Tests
# Student should not change this code.

def test(name, age):
    """Tests the name_and_age function."""
    
    print name_and_age(name, age)
    
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 52 years old.
#Scott Rixner is 40 years old.
#Error: Invalid age

###################################################
# 7.Write a Python fun print_digits that takes an integer number in the range [0,100) and prints the message "The tens digit
# is % and the ones digits is %" where the percents should be replaced with the appropriate values.The function should include
# an error check for the case when d is negative or greater than or equal to 100. In those cases, the function should instead 
# print "Error: Input is not a two-digit number.".

# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(number):
    if (0<number<=100):
        print "The tens digit is "+ str(number//10)+ " and the ones digits is " + str(number%10) + "."
    else:
        print "Error: Input is not a two-digit number."
    
###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.

###################################################
# 8. Write a Python function name_lookup that takes a string first_name that corresponds to one of ("Joe", "Scott", "John" 
# or "Stephen") and then returns their corresponding last name ("Warren", "Rixner", "Greiner" or "Wong"). If first_name 
# doesn't match any of those strings, return the string "Error: Not an instructor".
# Compute instructor's last name, given the first name.

###################################################
# Name lookup formula
# Student should enter function on the next lines.

def name_lookup(first_name):
    if (first_name=="Joe"):
        return "Warren"  
    elif (first_name=="Scott"): 
        return "Rixner"
    elif (first_name=="John"):
        return "Greiner"
    elif (first_name=="Stephen"):
        return "Wong" 
    else:
        return "Error: Not an instructor"
    

###################################################
# Tests
# Student should not change this code.

def test(first_name):
    """Tests the name_lookup function."""
    
    print name_lookup(first_name)
    
test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Warren
#Rixner
#Greiner
#Wong
#Error: Not an instructor

###################################################
# 9. Pig Latin is a language game that involves altering words via a simple set of rules. Write a Python function pig_latin 
# that takes a string word and applies the following rules to generate a new word in Pig Latin.
#
# If the first letter in word is a consonant, append the consonant plus "ay" to the end of the remainder of the word. For 
# example, pig_latin("pig") would return "igpay".
# If the first letter in word is a vowel, append "way" to the end of the word. For example, pig_latin("owl") returns "owlway".
# You can assume that word is in lower case.
# The provided template incl. code to extract the first letter and the rest of word in Python. Note that, in full Pig Latin, 
# the leading consonant cluster is moved to the end of the word. However, we don't know enough Python to implement full Pig 
# Latin just yet.

# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if (first_letter=="a" or first_letter=="e" or first_letter=="i" or first_letter=="o" or first_letter=="u"):
        return word + "ay"
    else:
        return rest_of_word + first_letter + "way"


###################################################
# Tests
# Student should not change this code.

def test(word):
    """Tests the pig_latin function."""
    
    print pig_latin(word)
    
test("pig")
test("owl")
test("python")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay

###################################################
# 10. Given numbers a, b, and c, the quadratic equation ax^2+b^x+c=0 can have zero, one or two real solutions 
# The expression b^2−4ac is the discriminant associated with the equation. If the discriminant is positive, the equation has 
# two solutions. If the discriminant is zero, the equation has one solution. Finally, if the discriminant is negative, the 
# equation has no solutions.

# Write a Python function smaller_root that takes an input the numbers a, b and c and returns the smaller solution to this 
# equation if one exists. If the equation has no real solution,print the message "Error: No real solutions" and simply return. 
# Note that, in this case, the function will actually return the special Python value None.
# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.
# Solution
def smaller_root(a, b, c):
    """
    Returns the smaller root of a quadratic equation with the
    given coefficients.
    """
    
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0 or a == 0:
        print "Error: No real solutions"
    else:
        discriminant_sqrt = discriminant ** 0.5
        # Choose the positive or negative square root that leads to a smaller root.
        if a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-b + smaller) / (2 * a)


###################################################
# Tests
# Student should not change this code.

def test(a, b, c):
    """Tests the smaller_root function."""
    
    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:" 
    print str(smaller_root(a, b, c))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None


