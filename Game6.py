# Mini-project #6 - Blackjack
#The Legend of Blackjack by Jose Angel
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images =simplegui.load_image("https://dl.dropboxusercontent.com/u/6543219/TLOZ.png?dl=1") #extension ?dl=1 tells dropbox that this file should be donwloadable

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back =simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")
                     
# initialize some useful global variables
in_play = False
outcome = ""
score = 0
                     
game_deck = []
player = []
dealer = []
                     
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10,
'J':10, 'Q':10, 'K':10}
                     
# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank
                     
    def __str__(self):
        return self.suit + self.rank
                     
    def get_suit(self):
        return self.suit
                     
    def get_rank(self):
        return self.rank
                     
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []
                     
    def __str__(self):
        # return a string representation of a hand
        res ="Hand contains "
        for card in self.hand:
            res += str(card)
            res += " "
                     
        return res
                     
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)
                     
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        has_aces = False

        for card in self.hand:
            value += VALUES[card.get_rank()]
            if (card.get_rank() == 'A'):
                has_aces = True

        if has_aces and (value+10 <= 21):
            value += 10

        return value
                     
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        position = pos
        for card in self.hand:
            card.draw(canvas, position)
            position[0] += 90
                     
# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []

        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit,rank)
                self.deck.append(card)
                     
    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck
        random.shuffle(self.deck)
                     
    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()

    def __str__(self):
        # return a string representing the deck
        res ="Deck contains "
        for card in self.deck:
            res += str(card)
            res += " "
                     
        return res

#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, player, dealer, score

    if in_play:
        score = score -1
        outcome = "You lose the round"
    else:
        outcome = ""
        in_play = True

    game_deck = Deck()
    game_deck.shuffle()

    player = Hand()
    dealer = Hand()
    player.add_card(game_deck.deal_card()) #1th card to player
    dealer.add_card(game_deck.deal_card()) #1th card to dealer
    player.add_card(game_deck.deal_card()) #2dn card to player
    dealer.add_card(game_deck.deal_card()) #2dn card to dealer

def hit():
    # replace with your code below
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global outcome, in_play, score

    if in_play:
        outcome = ""
        if player.get_value() <= 21:
            player.add_card(game_deck.deal_card())
        if player.get_value() > 21:
            outcome = "You have busted"
            in_play = False
            score = score -1

def stand():
    # replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global outcome, in_play, score

    if in_play:
        in_play = False
        if player.get_value() <= 21:
            while dealer.get_value() < 17:
                dealer.add_card(game_deck.deal_card())

            if dealer.get_value() > 21:
                outcome = "Dealer busts. You win"
                score += 1
            elif dealer.get_value() >= player.get_value():
                outcome = "You lose"
                score = score - 1
            else: #if player value > dealer value
                outcome = "You win"
                score += 1
        else:
            outcome = "You have busted"

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack",[175,50], 60,"Maroon")
    canvas.draw_text("Player",[50,390], 20,"Black")
    player.draw(canvas,[50,400])
    canvas.draw_text("Dealer",[50,220], 20,"Black")
    dealer.draw(canvas,[50,100])
    canvas.draw_text("Score: "+str(score),[200,550],30,"Black")
    canvas.draw_text(outcome,[175,350],40,"Olive")
    if in_play: #hide first dealer card
        canvas.draw_text("Hit or stand",[175,300],40,"Black")
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,[50+CARD_BACK_CENTER[0],100+CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        canvas.draw_text("New deal?",[175,300],40,"Black")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
                     
#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
deal()
                     
# get things rolling
frame.start()
