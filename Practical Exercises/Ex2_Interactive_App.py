
# Practice exercise for interactive applications

# 1. Write a Python function print_goodbye() that defines a local variable message whose value 
# is "Goodbye" and prints the value of this local variable to the console
# Printing "Goodbye" with a local message variable

###################################################
# Student should enter function on the next lines.

def print_goodbye():
    message = "Goodbye"
    print message

###################################################
# Tests

message = "Hello"
print message
print_goodbye()
print message

message = "Ciao"
print message
print_goodbye()
print message


###################################################
# Output

#Hello
#Goodbye
#Hello
#Ciao
#Goodbye
#Ciao

# 2. Write a Python function set_goodbye() that updates a global variable message with the value 
# "Goodbye" and prints the value of this global variable to the console. Note that the existing 
# global variable message has its original value "Hello" modified to "Goodbye" during the call to set_goodbye().
# Printing "Goodbye" with a global message variable

###################################################
# Student should enter function on the next lines.

def set_goodbye():
    global message
    message = "Goodbye"
    print message

###################################################
# Tests

message = "Hello"
print message
set_goodbye()
print message

message = "Ciao"
print message
set_goodbye()
print message


###################################################
# Output

#Hello
#Goodbye
#Goodbye
#Ciao
#Goodbye
#Goodbye

# 3. The function reset() sets the value of count to be zero,
# The function increment() adds one to count,
# The function decrement() subtracts one from count,
# The function print_count() that prints the value of count to the console.
# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
# Increment global count.
# Decrement global count.
# Print global count.
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
    
###################################################
# Test

# note that the GLOBAL count is defined inside a function
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
# Output
#1
#2
#-2

# 4. CodeSkulptor program opens a frame of size 100×200 with the title "My first frame".
# You will need to add only two extra lines of code.
# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

import simplegui ####### remember to import simplegui ######

message = "My first frame!"

# Handler for mouse click
def click():
    print message

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)

# Start the frame animation
frame.start()	####### remember to start the frame ######

# 5. Modify the program to create a CodeSkulptor frame that opens a 200×100 pixel frame with 
# the title "My second frame". Use the Docs to determine the correct syntax for the necessary SimpleGUI calls.
# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.
import simplegui

message = "My second frame!"

# Handler for mouse click
def click():
    print message
    
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [20,50], 24, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame(message, 200, 100)
frame.add_button("Click me", click)
frame.set_draw_handler(draw) # this draw out the red text

# Start the frame animation
frame.start()






