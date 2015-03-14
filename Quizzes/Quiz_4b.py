# Quiz 4b, Question 5
position1 = [50, 50]
delta1 = [1, -2]
position1 = position1 + delta1
print position1
# [50, 50, 1, -2]

print 
position2 = [50, 50]
delta2 = [1, -2]
position2[0] = position2[0] + delta2[0]
position2[1] = position2[1] + delta2[1]
print position2
# [51, 48]

# Quiz 4b, Question 6

a = ["green", "blue", "white", "black"]
print "a = " + str(a)                  
print
b = a                                
print "Are they the same: ", a is b    # Are they the same:  True
print
c = list(a)
print "Are they the same: ", a is c    # Are they the same:  False
print
d = c
print "Are they the same: ", d is c    # Are they the same:  True
print
a[3] = "red"
c[2] = a[1]
b = a[1 : 3]
b[1] = c[2]
print "Are they the same: ", b is c    # Are they the same:  False
print "Are they the same: ", b is a    # Are they the same:  False
print 
print "b = " + str(b)                  # b = ['blue', 'blue']

# There, there are 3 different lists being referred!

# Quiz 4b, Question 7
# Original version, press space-bar down will move the point.
# http://www.codeskulptor.org/#user39_5PqX3jJTBCIXiLi_12.py

import simplegui

POS = [10, 20]
chag = [3, 0.7]
WIDTH = 250
HEIGHT = 200
radius = 2
line_width = 4 
      
def keydown(key):
    # global POS
    if key == simplegui.KEY_MAP["space"]:
        POS[0] += chag[0]
        POS[1] += chag[1]
        
def draw_handler(canvas):
    canvas.draw_polygon([[50, 50], [180, 50], [180, 140], [50, 140]], line_width, 'Red')
    canvas.draw_circle(POS, radius, line_width, 'Green')
    
frame = simplegui.create_frame("Quiz4b, Q9", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw_handler)

frame.start()

# Modified version1, press space-bar down will stop the moving point.
# http://www.codeskulptor.org/#user39_5PqX3jJTBCIXiLi_11.py

import simplegui

POS = [10, 20]
chag = [3, 0.7]
WIDTH = 250
HEIGHT = 200
radius = 2
line_width = 4 

def keydown(key):
    global chag
    if key == simplegui.KEY_MAP["space"]: 
        chag = [0, 0]
        
def draw_handler(canvas):
    # global POS
    POS[0] += chag[0]
    POS[1] += chag[1]
    canvas.draw_polygon([[50, 50], [180, 50], [180, 140], [50, 140]], line_width, 'Red')
    canvas.draw_circle(POS, radius, line_width, 'Green')
 
frame = simplegui.create_frame("Quiz4b, Q9", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw_handler)

frame.start()

# Modified version2, press space-bar down will stop the moving point.
# http://www.codeskulptor.org/#user39_5PqX3jJTBCIXiLi_10.py

import simplegui

POS = [10, 20]
chag = [3, 0.7]
WIDTH = 250
HEIGHT = 200
radius = 2
line_width = 4
t_interval = 100

def timer():
    # global POS
    POS[0] += chag[0]
    POS[1] += chag[1]
    
def keydown(key):
    global chag
    if key == simplegui.KEY_MAP["space"]: 
        chag = [0, 0]
    
def draw(canvas):
    canvas.draw_polygon([[50, 50], [180, 50], [180, 140], [50, 140]], line_width, 'Red')
    canvas.draw_circle(POS, radius, line_width, 'Green')
    
frame = simplegui.create_frame("Quiz4b, Q9", WIDTH, HEIGHT)
timer = simplegui.create_timer(t_interval, timer)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

frame.start()
timer.start()

# Quiz 4b, Question 9
# http://www.codeskulptor.org/#user39_5PqX3jJTBCIXiLi_7.py

import simplegui

WIDTH = 200
HEIGHT = 100
var = 5

def keyup(key):
    global var
    if key == simplegui.KEY_MAP["space"]:
        var -= 3
        
def keydown(key):
    global var
    if key == simplegui.KEY_MAP["space"]:
        var *= 2
        
def draw(canvas):
    global var
    canvas.draw_text(str(var), [WIDTH/3, 2*HEIGHT/3], 40, "Red")
    
frame = simplegui.create_frame("Q9", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()

# Test
# 4 presses gives 35
# 12 presses gives 8195
