# implementation of card game - Memory

import simplegui
import random

card_size =[50,100]
half_card_width = card_size[0]/2
half_card_height = card_size[1]/2
counter = 0
state = 0
card1 = 0
card2 = 0

deck = range(8) + range(8)
exposed = range(len(deck))

# helper function to initialize globals
def init():
    global counter,state
    counter = 0
    state = 0
    random.shuffle(deck)
    for pos in range(len(deck)):
        exposed[pos] = False
        
    label.set_text("Moves = " + str(counter))
    
# define event handlers
def mouseclick(pos):
    global state,card1,card2,counter
    # add game state logic here
    click = list(pos)
    
    for n in range(len(deck)):
        if (click[0] >= 0+card_size[0]*n) and (click[0] < card_size[0]+card_size[0]*n):
            if not exposed[n]:
                if state == 0:
                    card1 = n
                    exposed[n] = True
                    state = 1
                elif state == 1:
                    card2 = n
                    exposed[n] = True
                    state = 2
                    counter += 1
                    label.set_text("Moves = " + str(counter))
                else:
                    if deck[card1] != deck[card2]:
                        exposed[card1] = False
                        exposed[card2] = False
                        
                    card1 = n
                    exposed[n] = True
                    state = 1

# cards are logically 50x100 pixels in size
def draw(canvas):
    for pos in range(len(deck)):
        point1 = (0+card_size[0]*pos ,0)
        point2 = (card_size[0]+card_size[0]*pos,0)
        point3 = (0+card_size[0]*pos ,card_size[1])
        point4 = (card_size[0]+card_size[0]*pos,card_size[1])
        
        if exposed[pos]:
            canvas.draw_polygon([point1,point2,point4,point3] , 2,"Black","Green")
            canvas.draw_text(str(deck[pos]),[card_size[0]/3 + card_size[0]*pos, card_size[1]*3/5], 40,"White")
        else:
            canvas.draw_polygon([point1,point2,point4,point3] ,2,"Black","Blue")

    # create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()