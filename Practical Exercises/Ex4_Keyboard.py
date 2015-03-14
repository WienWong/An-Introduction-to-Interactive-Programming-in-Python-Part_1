
# Practice exercises for keyboard

# Keyboard debugging 
# 1. The program template contains a program designed to echo the message "Pressed up arrow" or 
# "Pressed down arrow" whenever the appropriate key is pressed. Debug and fix the program.
# http://www.codeskulptor.org/#exercises_keyboard_debug_template.py

import simplegui

message = "Welcome!"

# Handler for keydown
def keydown(key):
    global message
    if key == "up":                      # <----- BUG HERE!
        message = "Up arrow" 
    elif key == "down":
        message = "Down arrow"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

############  Fixed version  ############

import simplegui

message = "Welcome!"

# Handler for keydown
def keydown(key):
    global message
    ####### Add KEY_MAP to translate to key codes
    if key == simplegui.KEY_MAP["up"]:
        message = "Up arrow"
    elif key == simplegui.KEY_MAP["down"]:
        message = "Down arrow"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
#### register the kedown handler
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


# Ball radius 1
# 2.Complete the program template below so that each press of the up arrow increases the radius
# of the white ball centered in the middle of the canvas by a small fixed amount and each press
# of the down arrow key decreases the radius of the ball by the same amount. Your added code
# should be placed in the keydown handler. (Note that draw_circle will throw an error if the 
# radius of the circle is decreased to zero or less.)

# My solution: http://www.codeskulptor.org/#user39_8KS4tGpMt8_0.py
import simplegui

WIDTH = 300
HEIGHT = 200
ball_radius = 50
BALL_RADIUS_INC = 3

# Handler for keydown
def keydown(key):
    global ball_radius
    if key == simplegui.KEY_MAP["up"]:
        ball_radius += BALL_RADIUS_INC
        if ball_radius > WIDTH / 2:        # <--- Stop increment
            ball_radius = WIDTH / 2        
    # Add code here to control ball_radius
    elif key == simplegui.KEY_MAP["down"]:
        ball_radius -= BALL_RADIUS_INC
        if ball_radius < 1:                # <--- Stop decrement
            ball_radius = 1

# Handler to draw on canvas
def draw(canvas):
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


# Space bar
# 3. Complete the program template so that the program displays "Space bar down" on the canvas while
# the space bar is held down and "Space bar up" while the space bar is up. You will need to add code
# to both the keydown and keyup handlers.

# My solution http://www.codeskulptor.org/#user39_Sh4b1bses8_1.py

# Space bar status

import simplegui

message = "Space bar up"

# Handlers for keydown and keyup
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar down"

def keyup(key):
    global message
    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar up"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [25, 112], 42, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


# Ball radius 2 
# 4. Complete the program template below so that holding down the up arrow key increases the radius
# of the white ball centered in the middle of the canvas by a small fixed amount each frame. Releasing
# the up arrow key causes that growth to cease. You will need to add code to the keydown and keyup 
# handlers as well as the draw handler. 

# My solution: http://www.codeskulptor.org/#user39_EDrnOeySz5_1.py

import simplegui

WIDTH = 300
HEIGHT = 200
ball_radius = 10
ball_growth = 0
BALL_GROWTH_INC = .2

# Handlers for keydown and keyup
def keydown(key):
    global ball_growth
    if key == simplegui.KEY_MAP["up"]: 
        ball_growth += BALL_GROWTH_INC
    elif key == simplegui.KEY_MAP["down"]: 
        ball_growth -= BALL_GROWTH_INC

def keyup(key):
    global ball_growth
    if (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        ball_growth = 0
    
# Handler to draw on canvas
def draw(canvas):
    global ball_radius
    ball_radius += ball_growth
    if ball_radius < 2:
        ball_radius = 2
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 2, "Red", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()









