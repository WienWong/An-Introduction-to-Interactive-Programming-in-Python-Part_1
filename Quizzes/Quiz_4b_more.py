
# More solutions to quiz 4b

#  Quiz4b, Question 7 

import simplegui

# initialize state
width = 200
height = 200
position = [10, 20]
radius = 2
velocity = [3,0.7]

# event handlers
def keydown(key):
    if key == simplegui.KEY_MAP['down']:
        position[1] = position[1] - velocity[1]
        position[0] = position[0] - velocity[0]
 
    elif key == simplegui.KEY_MAP['up']:
        position[1] = position[1] + velocity[1]
        position[0] = position[0] + velocity[0]
   
    
def draw(canvas):
    canvas.draw_circle(position, radius, 2, "red", "red")
    canvas.draw_line((50, 50), (50, 140), 2, "White")
    canvas.draw_line((50, 140), (180, 140), 2, "White")
    canvas.draw_line((180, 50), (50, 50), 2, "White")
    canvas.draw_line((180, 140), (180, 50), 2, "White")

# create frame
frame = simplegui.create_frame("Key Handling", width, height)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# start frame
frame.start()

###

# Quiz4b, Question 9

import simplegui

s = 5
counter=0

def keydown(key):
    global s
    if simplegui.KEY_MAP['s']:
        s = 2 * s
        
def keyup(key):
    global s, counter
    if simplegui.KEY_MAP['s']:
        s -= 3
    counter += 1 
    if counter==1:
        print str(counter) + " press gives " + str(s)
    elif counter > 1:
        print str(counter) + " presses give " + str(s)
        
frame = simplegui.create_frame('Testing', 100, 100)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
