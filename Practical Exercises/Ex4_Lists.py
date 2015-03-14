
# Practice exercises for lists

# Prime list 
# 1. Create a list that contains first 6 prime numbers in ascending order. (This list should 
# be created manually.) Print out the 2nd, 4th, and 6th numbers in this list.
lst = [2,3,5,7,11,13]
print lst[1], lst[3], lst[5]
# Expected output
#3 7 13

# List reference
# 2. Given the list a in the template, make a new reference b to a. Update the first entry in
# b to be zero. What happened to the first entry in a?
a = [5, 3, 1, -1, -3, 5]
b = a
b[0] = 0
print a
print b
# Explanation
# The assignment b = a created a second reference to a.
# Setting b[0] = 0 also mutated the list that both 
# a and b reference. As a result, a[0] == 0.

# List copy
# 3. Given the list a in the template, make a new copy b of the list a using the function list.
# Update the first entry in b to be zero. What happened to the first entry in a?
a = [5, 3, 1, -1, -3, 5]
b = list(a)
b[0] = 0
print a
print b
# Explanation
# The assignment b = list(a) created a copy of the list a.
# Setting b[0] = 0 only mutated the copy of the list, not
# the original list. As a result, a[0] == 5.

# Vector addition
# 4. Write a function add_vector(v, w) that takes two 2D vectors v and w (represented as lists)
# and returns a new 2D vector (represented as a list) that is the sum of the two vectors. 
def add_vector(v,w):
    addition = [v[0] + w[0], v[1] + w[1]]
    return addition
# Test
print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])

# Debugging test
# 5. The program template below is a program designed to run two independent timers with their
# own start and stop buttons. In particular, each timer should be controlled by its own buttons
# independent of the other timer's buttons. The current version has an error that causes both 
# timers to work in unison. Find and fix this error.
# template: http://www.codeskulptor.org/#exercises_lists_debug_template.py

# Mystery bug

import simplegui

# Initialize two counters.
counter1 = [0, 0]
counter2 = counter1                          # <-------- BUG HERE!

# Define event handlers.
def start1():
    timer1.start()
    
def stop1():
    timer1.stop()
    
def start2():
    timer2.start()
    
def stop2():
    timer2.stop()
    
def tick1():
    global counter
    if counter1[1] == 9:
        counter1[0] += 1
        counter1[1] = 0
    else:
        counter1[1] += 1

def tick2():
    global counter
    if counter2[1] == 9:
        counter2[0] += 1
        counter2[1] = 0
    else:
        counter2[1] += 1
                
# Define draw handler.
def draw(canvas):
    canvas.draw_text("Timer 1:     " + str(counter1[0] % 10) + "." + str(counter1[1]), [50, 100], 24, "White")
    canvas.draw_text("Timer 2:     " + str(counter2[0] % 10) + "." + str(counter2[1]), [50, 200], 24, "White")

# Register event handlers.
frame = simplegui.create_frame("Mystery bug", 300, 300)
frame.add_button("Start timer1", start1, 200)
frame.add_button("Stop timer1", stop1, 200)
frame.add_button("Start timer2", start2, 200)
frame.add_button("Stop timer2", stop2, 200)
frame.set_draw_handler(draw)

timer1 = simplegui.create_timer(100, tick1)
timer2 = simplegui.create_timer(100, tick2)

# Start frame.
frame.start()

# # # Fixed version

import simplegui

# Initialize two counters.
counter1 = [0, 0]
counter2 = list(counter1)                    # <-------- FIXED HERE!

# Define event handlers.
def start1():
    timer1.start()
    
def stop1():
    timer1.stop()
    
def start2():
    timer2.start()
    
def stop2():
    timer2.stop()
    
def tick1():
    global counter
    if counter1[1] == 9:
        counter1[0] += 1
        counter1[1] = 0
    else:
        counter1[1] += 1

def tick2():
    global counter
    if counter2[1] == 9:
        counter2[0] += 1
        counter2[1] = 0
    else:
        counter2[1] += 1
                
# Define draw handler.
def draw(canvas):
    canvas.draw_text("Timer 1:     " + str(counter1[0] % 10) + "." + str(counter1[1]), [50, 100], 24, "White")
    canvas.draw_text("Timer 2:     " + str(counter2[0] % 10) + "." + str(counter2[1]), [50, 200], 24, "White")

# Register event handlers.
frame = simplegui.create_frame("Mystery bug", 300, 300)
frame.add_button("Start timer1", start1, 200)
frame.add_button("Stop timer1", stop1, 200)
frame.add_button("Start timer2", start2, 200)
frame.add_button("Stop timer2", stop2, 200)
frame.set_draw_handler(draw)

timer1 = simplegui.create_timer(100, tick1)
timer2 = simplegui.create_timer(100, tick2)

# Start frame.
frame.start()

# Solution gives:
counter1 = [0, 0]
##### The bug was here. In the template, we create two references to a single list.
counter2 = [0, 0]
##### Making two distinct lists resolves the issue.  
