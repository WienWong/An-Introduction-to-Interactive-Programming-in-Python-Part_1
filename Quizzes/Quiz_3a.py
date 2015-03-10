
# 4. Assume we have a canvas that is 200 pixels wide and 300 pixels high. We want to draw a green line between the upper left
# corner and the lower right corner.

import simplegui

#define draw handler
def draw(canvas):
    #canvas.draw_line((200, 300), (0, 0), 10, "Green")  # Or
    canvas.draw_line((199, 299), (0, 0), 10, "Green")
    
    # Green line between the upper right corner and the lower left corner. 
    #canvas.draw_line((199, 0), (0, 299), 10, "Green")
#create frame
myframe = simplegui.create_frame("Drawing", 200, 300)

# register event handlers
myframe.set_draw_handler(draw)

#start frame
myframe.start()

# 5. Consider the following function definition.

def date(month, day):
    """
    Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day.
    """
    return str(month) + "/" + str(day)

print date(2, 12)

# Line 6: TypeError: cannot concatenate 'str' and 'int' objects
# To fix it,

def date(month, day):
    """
    Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day.
    """
    return str(month) + "/" + str(day)

print date(2, 12)

# 6a. Assume we have a variable word that contains a string, such as "Mississippi" or "indivisible". We would like to determine
# how many "i"'s are in the string word. What code should replace the question marks in the following function definition?

def number_of_i(word):
    """Returns the number of lower-case i's in the word."""
    return ???

# Code should be    
def number_of_i(word):
    """Returns the number of lower-case i's in the word."""
    return word.count("i")

word = "Mississippi"
print number_of_i(word)

# 6b. How many instances of the letter "l" are there in the following:

1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1
# Although it might be hard to tell, that string contains ones (1) and lower-case L's (l).

# Code should be    
def number_of_l(word):
    """Returns the number of lower-case i's in the word."""
    return word.count("l")

word = "1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1"
print number_of_l(word)  # 60

# 9. Turn the following description into a CodeSkulptor program, and run it.
# Create a 300-by-300 canvas.
# Draw two circles with radius 20 and white lines of width 10. One is centered at (90,200) and one at (210,200).
# Draw a red line of width 40 from (50,180) to (250,180).
# Draw two red lines of width 5 from (55,170) to (90,120) and from (90,120) to (130,120).
# Draw a red line of width 140 from (180,108) to (180,160).
# The resulting picture is a simple diagram of what?

import simplegui

# define fraw handler
def draw(canvas):
    canvas.draw_circle((90, 200), 20, 10, 'White')
    canvas.draw_circle((210, 200), 20, 10, 'White')
    canvas.draw_line((50,180), (250,180), 40, 'Red')
    canvas.draw_line((55,170), (90,120), 5, 'Red')
    canvas.draw_line((90,120), (130,120), 5, 'Red')
    canvas.draw_line((180,108), (180,160), 140, 'Red')

# create frame
myframe = simplegui.create_frame("Drawing", 300, 300)

# register event handlers
myframe.set_draw_handler(draw)

# start frame
myframe.start()

