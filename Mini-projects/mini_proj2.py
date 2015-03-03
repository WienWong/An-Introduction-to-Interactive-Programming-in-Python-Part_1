
# mini-project2  "Guess the number" 
# input will come from buttons and an input field
# all output for the game will be printed in the console

# project basic template   http://www.codeskulptor.org/#examples-guess_the_number_template.py
# project testing template http://www.codeskulptor.org/#examples-gtn_testing_template.py

import simplegui
import math
import random


# helper function to start and restart the game
counter = 10
num_range = 1000

def new_game():
    # initialize global variables used in your code here
    global secret_number, counter # What happen if 'counter' was Not been set as global variable?
    secret_number = random.randrange(0, num_range)
    
    if num_range == 100:
        counter = 7
    elif num_range == 1000:
        counter = 10

    print
    print "New game. Range is from 0 to " + str(num_range)
    print "Number of remaining guesses is " + str(counter)

    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()

def input_guess(guess):
    # main game logic goes here	
    global counter 
    guessnum = int(guess)       
    print     
    print "Guess was", guessnum
    
    if num_range == 1000:
        if (guessnum >= 1000 or guessnum < 0):
            print "Invalid Guess Number! Number Range Should Be [0, 1000)."
            
        if counter > 0:
            counter -= 1
            print "Number of remaining guess is", counter  
      
            if guessnum < secret_number:
                print "Higher!"
            elif guessnum > secret_number:
                print "Lower!"
            else:
                print "Correct!"
                new_game()
        else:
            print
            print "You ran out of guess. Guess was", secret_number
            new_game()
    

    elif num_range == 100:
        if (guessnum >= 100 or guessnum < 0):
            print "Invalid Guess Number! Number Range Should Be [0, 100)."
            
        if counter > 0: 
            counter -= 1
            print "Number of remaining guess is", counter  

            if guessnum < secret_number:
                print "Higher!"
            elif guessnum > secret_number:
                print "Lower!"
            else:
                print "Correct!"
                new_game()            
        else:
            print "You ran out of guess. Guess was", secret_number
            new_game()
    
# create frame
myframe = simplegui.create_frame("Guess Game", 100, 200)

# register event handlers for control elements and start frame
myframe.add_input("AddInput:", input_guess, 120)
myframe.add_button("Range is [0,100)", range100, 120)
myframe.add_button("Range is [0,1000)", range1000, 120)
myframe.start()

# call new_game 
new_game()


