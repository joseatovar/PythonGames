# Implementation of classic arcade game Pong
#Jose Angel
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
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0,0]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
vel = 10

# helper function that spawns a ball by updating the
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120, 240) / 60 #you need to divide it by 60 because the screen refreshes 60 times per second with the simplegui.
    if not right:
        ball_vel[0] = -ball_vel[0] #if right == False then velocity is upper left
    ball_vel[1] = -random.randrange(60, 180) / 60 #you need to divide it by 60 because the screen refreshes 60 times per second with the simplegui.
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # these are floats
    global score1, score2 # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    ball_init(True)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_pos - HALF_PAD_HEIGHT + paddle1_vel) >= 0 and (paddle1_pos +
    HALF_PAD_HEIGHT + paddle1_vel) <= HEIGHT:
        paddle1_pos += paddle1_vel
    if(paddle2_pos - HALF_PAD_HEIGHT + paddle2_vel) >= 0 and (paddle2_pos +
    HALF_PAD_HEIGHT + paddle2_vel) <= HEIGHT:
        paddle2_pos += paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #paddle 1
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],
    [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    #paddle 2
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH
    - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # update ball
    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
    #collision code for top and bottom
        ball_vel[1] = -ball_vel[1]
    if (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH): #collision code for left gutters
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <=
        paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = ball_vel[0] + (ball_vel[0]*0.1)
            ball_vel[0] = -ball_vel[0]
        else:
            score2 = score2 + 1
            ball_init(True)
    if (ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH): #collision code for right gutters
        if(ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <=
        paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = ball_vel[0] + (ball_vel[0]*0.1)
            ball_vel[0] = -ball_vel[0]
        else:
            score1 = score1 + 1
            ball_init(False)
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball and scores
    #ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    #score 1
    c.draw_text(str(score1),[200,70],40,"White")
    #score 2
    c.draw_text(str(score2),[400,70],40,"White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= vel
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += vel
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset",new_game,100)
# start frame
frame.start()
new_game()