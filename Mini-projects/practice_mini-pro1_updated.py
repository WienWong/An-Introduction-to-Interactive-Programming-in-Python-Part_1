
# An updated version for practice mini-project 1 using dictionary.

# First comes my solution

import random

num2fortune = {
    "Yes, for sure!"              : 0,
    "Probably yes."               : 1,
    "Seems like yes..."           : 2,
    "Definitely not!"             : 3,
    "Probably not."               : 4,
    "I really doubt it..."        : 5,
    "Not sure, check back later!" : 6,
    "I really can't tell"         : 7,
    "Input out of range."         : 8,
    };

def mystical_octosphere(question):
    print question
    print "You shake the mystical octosphere."
    answer_number = random.randrange(0,9)
    answer_fortune = None
    for key, value in num2fortune.items():
        if (value == answer_number):
            answer_fortune = key
    print "The cloudy liquid swirls, and a reply comes into view..."
    print "The mystical octosphere says... " + answer_fortune
    print

mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?") 

# Flaw: cannot handle numbers out of range, for example a random number 100 was selected.
# Attach another version of code comes from the course forum.

import random

def number_to_fortune(number):
    if number not in range(8):
        return "Input out of range: %d" %number
    
    octosphere_dict = {0    : "Yes, for sure!",
                       1    : "Probably yes.",
                       2    : "Seems like yes...",
                       3    : "Definitely not!",
                       4    : "Probably not.",
                       5    : "I really doubt it...",
                       6    : "Not sure, check back later!",
                       7    : "I really can't tell",                       
                       }
    
    return octosphere_dict[number]

def mystical_octosphere(question):
    print question
    print "You shake the mystical octosphere."
    answer_number = random.randrange(8)
    answer_fortune = number_to_fortune(answer_number)
    print "The cloudy liquid swirls, and a reply comes into view..."
    print "The mystical octosphere says..."
    print answer_fortune
    
qst = raw_input("Enter your question.")
mystical_octosphere(qst)
