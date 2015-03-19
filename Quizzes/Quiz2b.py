
# Quize 2b, Question 3  valid ways of defining and using a label
# Wrong option
# import simplegui
#
# def label_handler():
#    print "Handler called."
#
# f = simplegui.create_frame('Testing', 100, 100)
# f.add_label("My label",label_handler) # error here
# TypeError: width must be an integer

# Right option
import simplegui
f = simplegui.create_frame('Testing', 100, 100)
label = f.add_label("My label")
label.set_text("My new label")

# Wrong option 
# import simplegui
# simplegui.create_frame('Testing', 100, 100)
# simplegui.add_label("My label")
# AttributeError: '<invalid type>' object has no attribute 'add_label'

# Right option
import simplegui
frame = simplegui.create_frame('Testing', 100, 100)
frame.add_label("Label one")
frame.add_label("Label two")

# Quiz 2b, Question 6  Any mistake in the following code?

#def volume_cube(side):
#    """ Returns the volume of a cube, given the length of its side. """
#    print side ** 3
#
#s = 5
#print "The volume of a cube with sides", s, "long is", volume_cube(s), "."

# 'return' should be added, thus:
def volume_cube(side):
    """ Returns the volume of a cube, given the length of its side. """
    return side ** 3

s = 5
print "The volume of a cube with sides", s, "long is", volume_cube(s), "."

# Quiz 2b, Question 5

def compare(p, q):
    if p == False:
        return False
    elif q == False:
        return False
    else:
        return True
    
print compare(False, False)
print compare(False, True)
print compare(True, False)
print compare(True, True)

print

def compare2(x,y):
    #return x and y
    #return not(x or y)
    #return x and (not y)
    return (not x) or (not y) # it gives same result!

print compare(False, False)
print compare(False, True)
print compare(True, False)
print compare(True, True)


print

def compare2(x,y):
    return x and y # it gives same result!

print compare(False, False)
print compare(False, True)
print compare(True, False)
print compare(True, True)


# Quiz 2b, Question 9

# Simple interactive application

import simplegui

# Define globals.

message = "Welcome!"
count = 0

# Define event handlers.

def button_handler():
    """Count number of button presses."""
    global count
    count += 1
    print message,"  You have clicked", count, "times."
    
def input_handler(text):
    """Get text to be displayed."""
    global count, message
    count = 0
    message = text

# Create frame and register event handlers.

frame = simplegui.create_frame("Home", 100, 200)
frame.add_button("Click me", button_handler)
frame.add_input("New message:", input_handler, 100)

# Start frame.

frame.start()

