
# Practice exercises for buttons and input fields

# 1. Write event handlers print_hello() and print_goodbye() for the two buttons with labels
# "Hello" and "Goodbye" defined in the program template below. Pressing these buttons should
# print the messages "Hello" and "Goodbye", respectively, in the console.
# Add "Hello" and "Goodbye" buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 


# Handlers for buttons
def print_hello():
    print "hello"
    
def print_goodbye():
    print "goodbye"

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)


# Start the frame animation
frame.start()


###################################################
# Test

print_hello()
print_hello()
print_goodbye()
print_hello()
print_goodbye()

###################################################
# Expected output from test

#Hello
#Hello
#Goodbye
#Hello
#Goodbye

# 2. Given the three function print_color(), set_red(), and set_blue() in the program template 
# below, create three buttons that print and manipulate the global variable color. 
# Register three buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 


# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print color

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)
frame.add_button("Set2red", set_red)
frame.add_button("Set2blue", set_blue)
frame.add_button("Printcolor", print_color)


# Start the frame animation
frame.start()


###################################################
# Test

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

###################################################
# Expected output from test

#red
#blue
#blue

# 3. Implement four buttons that manipulate a global variable count as follows:
# The function reset() sets the value of count to be zero,
# The function increment() adds one to count,
# The function decrement() subtracts one from count,
# The function print_count() prints the value of count to the console.

# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simplegui

# Define event handlers for four buttons

count = 0

def reset():
    global count
    count = 0
  
def increment():
    global count
    count += 1
    
def decrement():
    global count
    count -= 1
    
def print_count():
    print count

    
# Create frame and assign callbacks to event handlers
myframe = simplegui.create_frame("My frame", 150, 150)
myframe.add_button("Reset", reset)
myframe.add_button("Incre", increment)
myframe.add_button("Decre", decrement)
myframe.add_button("Print", print_count)

# Start the frame animation
myframe.start()

    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2

# 4. Write a program that creates an input field and echoes input to that field to the console.
# Echo an input field

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Handlers for input field
def get_input(text):
    print text
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_input("First test input")
get_input("Second test input")
get_input("Third test input")

###################################################
# Expected output from test

#First test input
#Second test input
#Third test input

# 5. Write a program allows a user to enter a word in an input field, translates that word into 
# Pig Latin and prints this translation in the console. For the sake of modularity, we suggest 
# that you build a helper function that handles all of the details of translating a word to 
# Pig Latin (see the practice exercises for logic and conditionals) . 
# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if (first_letter=="a" or first_letter=="e" or first_letter=="i" or \
        first_letter=="o" or first_letter=="u"):
        return word + "way"
    else:
        return rest_of_word + first_letter + "ay"

# Handler for input field
def get_input(text):
    print pig_latin(text)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Add text (hit enter)", get_input, 200)

# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay

# 6. Add an interactive user interface for your implementation of "Rock-paper-scissors-lizard-Spock". 
# Create an input field that takes a player's guess, generates a random computer guess, and prints out 
# the player and computer choices as well as who won in the console. 

# http://www.codeskulptor.org/#exercises_button_rpsls_template.py

# GUI-based version of RPSLS template

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS

     
    
# Handler for input field
def get_guess(guess):
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#

# # # My code link http://www.codeskulptor.org/#user39_rnSxBIHD9d_3.py

# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS

# Helper functions

def name_to_number(name):
    # It converts the string name into a number between 0 and 4 using if/elif/else
    # Don't forget to return the result!
    
    if name == "rock":
        num = 0
    elif name == "Spock":
        num = 1
    elif name == "paper":
        num = 2
    elif name == "lizard":
        num = 3
    elif name == "scissors":
        num = 4
    else:
        print "Not match, error."
    return num

def number_to_name(number):
    # It converts a number in the range 0 to 4 into its corresponding name as a string using if/elif/else.
    # Don't forget to return the result!
    
    if number == 0:
        nam = "rock"
    elif number == 1:
        nam = "Spock"
    elif number == 2:
        nam = "paper"
    elif number == 3:
        nam = "lizard"
    elif number == 4:
        nam = "scissors"
    else:
        print "Number out of range."
    return nam
    
# Handler for input field and main body of omputing RPSLS  
        
def get_guess(guess):            
    # Print a blank line to separate consecutive games
    print 
    
    if (guess=="rock" or guess=="Spock" or guess=="paper" or guess=="lizard" or guess=="scissors"):
        print "Player inputs: " + guess
    else:
        print "Error: Bad input " + guess + " to rpsls"   
        return guess
    
    # Convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(guess)
    
    # Compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # Convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # Print out the message for computer's choice
    print "Computer chooses: " + comp_choice
    
    # Compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5

    # Use if/elif/else to determine winner, print winner message
    if diff == 1 or diff == 2:
        print "Computer wins!"
    elif diff == 3 or diff == 4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#

# # # Solution link http://www.codeskulptor.org/#exercises_button_rpsls_solution.py

# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Insert your solution for RPSLS here
# Helper functions

def name_to_number(name):
    # It converts the string name into a number between 0 and 4 using if/elif/else
    # Don't forget to return the result!
    
    if name == "rock":
        num = 0
    elif name == "Spock":
        num = 1
    elif name == "paper":
        num = 2
    elif name == "lizard":
        num = 3
    elif name == "scissors":
        num = 4
    else:
        print "Not match, error."
    return num

def number_to_name(number):
    # It converts a number in the range 0 to 4 into its corresponding name as a string using if/elif/else.
    # Don't forget to return the result!
    
    if number == 0:
        nam = "rock"
    elif number == 1:
        nam = "Spock"
    elif number == 2:
        nam = "paper"
    elif number == 3:
        nam = "lizard"
    elif number == 4:
        nam = "scissors"
    else:
        print "Number out of range."
    return nam
    
def rpsls(player_choice):     
    # Print a blank line to separate consecutive games
    print 
    
    # Print out the message for the player's choice
    print "Player chooses: " + player_choice
    
    # Convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # Compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # Convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # Print out the message for computer's choice
    print "Computer chooses: " + comp_choice
    
    # Compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5

    # Use if/elif/else to determine winner, print winner message
    if diff == 1 or diff == 2:
        print "Computer wins!"
    elif diff == 3 or diff == 4:
        print "Player wins!"
    else:
        print "Player and computer tie!"

 
# handler for input field
def get_guess(guess):
    
    # validate input
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#




