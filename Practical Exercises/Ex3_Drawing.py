
# Practice exercises for drawing

# 1. Modify the following program template to print "It works!" on the canvas.
# Print to canvas

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)

# register event handler
frame.set_draw_handler(draw)

# start frame
frame.start()

# 2. Add draw commands to the draw handler to draw "This is easy?" on the canvas.
# Display "This is easy?"

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("This is easy", [100, 100], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()

# 3. Create a canvas of size 96×96, and draw the letter "X" with font size 48 in the upper left portion of the canvas.
# Display an X

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    # Note that vertical position for the text was computed manually
    canvas.draw_text("X", [0, 32], 48, "Red")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Display", 96, 96)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

# 4. Write a function format_time that takes an integer number of seconds in range(0, 3600) and converts it into string that states the number of minutes and seconds. Remember to use the operations // and %.

# Define a function that returns formatted minutes and seconds

###################################################
# Circle area formula
# Student should enter function on the next lines.
def format_time(secinp):
    mint = secinp // 60
    secd = secinp % 60
    return str(mint) + " minutes and " + str(secd) + " second"

###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds

# 5. Complete the program template below and add two buttons that control the radius of a white ball centered in the middle of the canvas. Clicking the “Increase radius” button should increase the radius of the ball. Clicking the “Decrease radius” button should decrease the radius of the ball, except that the ball radius should always be positive.

# Ball radius template  http://www.codeskulptor.org/#exercises_drawing_ball_template.py

# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    # global ball_radius  # you don't need this global var here.
    canvas.draw_circle([WIDTH/2 - 1, HEIGHT/2 - 1], ball_radius, 8, 'Red')

# Solution use:
# def draw(canvas):
#     canvas.draw_circle([WIDTH // 2, HEIGHT // 2], ball_radius, 1, "White", "White")
    
# Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius += RADIUS_INCREMENT

def decrease_radius():
    global ball_radius
    if ball_radius > RADIUS_INCREMENT:
        ball_radius -= RADIUS_INCREMENT

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)


# Start the frame animation
frame.start()


