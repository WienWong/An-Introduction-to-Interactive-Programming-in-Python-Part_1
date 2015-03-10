
# Practice exercises for timers (should be Ex3!)

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

# 5. Challenge: Use a timer to measure how fast you can press a button twice. Create a button that starts a timer that ticks 
# every hundredth of a second. The first button press starts the measurement. The second button press ends the measurement. 
# Print to the console the time elapsed between button presses. The next two button presses should repeat this process, making
# a new measurement. Hint: We suggest that you keep track of whether the program is on the first or second button press using
# a global Boolean variable.

# My solution
# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 
import time

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks, time1
    total_ticks += 1
 

# Button handler
def click():
    global first_click, time1, time2
    if first_click:
        timer.start()
        time1 = time.time(0)
        first_click=False
    else:
        timer.stop()
        time2 = time.time()
        print 'Time elapsed:', time2 - time1
        first_click=True
  

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(1000, tick)

# Start timer
frame.start()
timer.start()

# Teacher solution
# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Button handler
def click():
    global total_ticks, first_click
    if first_click:
        first_click = False
        total_ticks = 0
        timer.start()
    else:
        first_click = True
        timer.stop()
        print "Time between clicks is " + str(total_ticks / 100.0) + " seconds"
        total_ticks = 0

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
timer.start()
