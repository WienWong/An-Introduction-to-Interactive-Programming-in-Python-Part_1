
# Mini-project 3 -- "Stopwatch: The Game"
# Run the final version in CodeSkulptor at http://www.codeskulptor.org/#user39_86y6oVX8va_5.py
# mini-project 3 template: http://www.codeskulptor.org/#examples-stopwatch_template.py
# 'format' testing template: http://www.codeskulptor.org/#examples-format_template.py

import simplegui

# define global variables
ticks = 0
WIDTH = 200
HEIGHT= 200
position = [WIDTH/4 - 10, 3*HEIGHT/5 - 1]
counter1 = 0                    # number of successful stops 
counter2 = 0                    # number of total stops 
place1 = [3*WIDTH/5, 30]        # location of "X" -- successful stops
place2 = [3*WIDTH/5 + 13, 30]   # location of "/"
place3 = [3*WIDTH/5 + 20, 30]   # location of "Y" -- total stops

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
    
def format(t):
    A = t // 600
    B = t % 600 //100
    C = t % 100 //10  
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
# Hint from the forum    
# In your stop button handler, if the stopwatch has already been stopped 
# you should do nothing at all - that can be done by making the code:

#if not timer.is_running() then
#	return

# Code to execute when timer is running
# ...
    
def stop():
    global ticks, counter1, counter2
    if not timer.is_running():  
        return  
    timer.stop()
    counter2 += 1
    if ticks%10 == 0: 
        counter1 += 1
            
def reset():
    global ticks, counter1, counter2
    timer.stop()
    ticks = 0
    counter1 = 0
    counter2 = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global ticks
    ticks += 1
    return ticks
    
# define draw handler
def draw(canvas):
    message = str(format(ticks))
    canvas.draw_text(message, position, 48, "Red")
    canvas.draw_text(str(counter1), place1, 24, "Yellow")
    canvas.draw_text("/", place2, 24, "Yellow")
    canvas.draw_text(str(counter2), place3, 24, "Yellow")
    
# create frame
myframe = simplegui.create_frame("Stop and Watch", WIDTH, HEIGHT)

# register event handlers
myframe.set_draw_handler(draw)
myframe.add_button("Start", start, 100)
myframe.add_button("Stop", stop, 100)
myframe.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)

# start frame
myframe.start()
# timer.start()  # Don't want the timer to start automatically


