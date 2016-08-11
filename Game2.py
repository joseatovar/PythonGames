# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
rangeDown = 0
rangeUp = 100
secretNumber = 0
numberGuesses = 0

def number_guesses(ini,end):
    return math.ceil(math.log(end - ini + 1,2)) # 2 ** number_guesses >= end -ini + 1

def range100():
    # button that changes range to range [0,100) and restarts
    global rangeUp
    
    rangeUp = 100
    init()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global rangeUp
    
    rangeUp = 1000
    init()
    
def get_input(guess):
    global numberGuesses
    playerNumber = math.floor(float(guess))
    numberGuesses = numberGuesses - 1
    print "Guess was ",playerNumber
    print "Number of remaining guesses is ",numberGuesses
    if playerNumber == secretNumber:
        print "Correct!"
        print
        init()
    elif numberGuesses > 0 and playerNumber > secretNumber:
        print "Lower!"
    elif numberGuesses > 0 and playerNumber < secretNumber:
        print "Higher!"
    else:
        print "You failed, secret number is ", secretNumber
        print
        init()
    print
    
def init():
    global secretNumber,numberGuesses
    secretNumber = random.randrange(rangeDown, rangeUp)
    numberGuesses = number_guesses(rangeDown, rangeUp)
    print "New game. Range is from 0 to ",rangeUp
    print "Number of remaining guesses is ",numberGuesses
    print

# create frame
frame = simplegui.create_frame("Guess the number",200,200)
# register event handlers for control elements
frame.add_button("Range is [0-100)",range100,200)
frame.add_button("Range is [0-1000)",range1000,200)
frame.add_input("Enter a guess",get_input,200)
# start frame
frame.start()
init()