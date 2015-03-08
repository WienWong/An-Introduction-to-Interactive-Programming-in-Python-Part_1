
# Practice exercises for timers

# 1. The following program should count upward from zero. Print the counter values 0, 1, 2, … to the console.
# Counter ticks

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()

# 2. Add three buttons that start, stop and reset the counter, respectively.
# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons    
def start():
    timer.start()
    
def stop():
    timer.stop()

def reset():
    global counter
    counter = 0
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()

# 3. Use a timer to toggle the canvas background back and forth between red and blue every 3 seconds. 
# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

color = "Red"
counter = 0

# Timer handler
def tick():
    global color, counter
    if color == "Red":
        color = "Blue"
    else:
        color = "Red"
    frame.set_canvas_background(color)
    counter += 1
    print counter

def stop():
    timer.stop()
    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)
frame.set_canvas_background(color)
frame.add_button("Stop", stop)

# Start timer
frame.start()
timer.start()

# 4. Create a circle in the center of the canvas. Use a timer to increase its radius one pixel every tenth of a second.
# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def tick():
    global radius
    radius += 1
    
# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH // 2 - 1, HEIGHT // 2 - 1], radius, 4, "Red")
        
# Create frame and timer
frame = simplegui.create_frame("Frame", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# Start timer
frame.start()
timer.start()

# 5. 
