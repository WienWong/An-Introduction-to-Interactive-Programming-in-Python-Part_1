
# mini-project4  "Pong" 
# project basic template   http://www.codeskulptor.org/#examples-pong_template.py
# My original code link    http://www.codeskulptor.org/#user39_4QBbwORHtE_8.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [2, 2]
# paddle1_pos, paddle2_pos, paddle1_vel and paddle2_vel should be numbers, NOT lists. 
# Making them list causes needless complexity and is highly UNrecommended. 
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
CONST = 0.02      # this controls the spawnning speed.


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == RIGHT:
        ball_vel[0] = CONST * random.randrange(60, 180)   		  # vertical velocity
        ball_vel[1] = -CONST * random.randrange(120, 240) 		  # horizontal velocity
    if direction == LEFT:
        ball_vel[0] = -CONST * random.randrange(60, 180)    
        ball_vel[1] = -CONST * random.randrange(120, 240)
 
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel   # these are numbers
    global score1, score2                                       # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    score1 = 0  			# score of left paddle
    score2 = 0  			# score of right paddle
    spawn_ball(LEFT)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel

 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
        
    # update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  
    
    
    # determine whether paddle and ball collide  
    if (ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)):
        if (ball_pos[1] < (paddle1_pos - HALF_PAD_HEIGHT)) or (ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT)):
            score2 += 1
            spawn_ball(RIGHT)  
        else:  
            ball_vel[0] = - ball_vel[0] * 1.1  	# flip horizontal component of velocity!
   
    
    # My previous logic for paddle 1
#    if (ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)):
#        if (ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT)) or (ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT)):  
#            ball_vel[0] = - ball_vel[0] * 1.1  # flip horizontal component of velocity!
#        elif (ball_pos[1] < (paddle1_pos - HALF_PAD_HEIGHT)) or (ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT)):
#            score2 += 1
#            spawn_ball(RIGHT)  

   
    if (ball_pos[0] >= (WIDTH - 1 - PAD_WIDTH) - BALL_RADIUS):
        if (ball_pos[1] < (paddle2_pos - HALF_PAD_HEIGHT)) or (ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT)):
            score1 += 1
            spawn_ball(LEFT)            
        else:  
            ball_vel[0] = - ball_vel[0] * 1.1 	 # flip horizontal component of velocity!

            
    # My previous logic for paddle 2       
#    if (ball_pos[0] >= (WIDTH - 1 - PAD_WIDTH) - BALL_RADIUS):
#        if (ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT)) or (ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT)):  
#            ball_vel[0] = - ball_vel[0] * 1.1 # flip horizontal component of velocity!
#        elif (ball_pos[1] < (paddle2_pos - HALF_PAD_HEIGHT)) or (ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT)):
#            score1 += 1
#            spawn_ball(LEFT)


    # determine whether ball collide with bottom and upper boundary  
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1] # flip vertical component of velocity!
 
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Blue")
    #canvas.draw_circle([WIDTH / 2,HEIGHT / 2], BALL_RADIUS, 2, "Red", "Blue")   # why this not work?  
    
    
    # update paddle's vertical position       
    if (paddle1_pos >= HALF_PAD_HEIGHT) or (paddle1_pos <= HEIGHT - 1 - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
                                           
    if (paddle2_pos >= HALF_PAD_HEIGHT) or (paddle2_pos <= HEIGHT - 1 - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel

        
    # keep paddle on the screen
    if paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos > HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - 1 - HALF_PAD_HEIGHT
        
    if paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos > HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - 1 - HALF_PAD_HEIGHT
    
    
    # draw paddles
    # Note that paddle1_pos = HEIGHT / 2, paddle2_pos = HEIGHT / 2
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH/2, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH / 2, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]], 10, 'Red')
    canvas.draw_polygon([[WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH / 2, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH / 2, paddle2_pos - HALF_PAD_HEIGHT]], 10, 'Red')
    

    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2 - 30, 50), 36, "Yellow")
    canvas.draw_text(str(score2), (WIDTH / 2 + 15, 50), 36, "Yellow") 
   
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 3                          # this controls the moving paddle responding velocity
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc

    
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 0
    if (key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = acc
    elif (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = acc
  
     
def reset():
    new_game()
    
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', reset, 100)

# start frame
new_game()
frame.start()
