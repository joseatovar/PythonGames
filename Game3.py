#"Stopwatch: The Game"
#Jose Angel
import simplegui
# define global variables
time = 0
score = 0
stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenthSec = t%10
    sec = t//10 #integer division
    mins = sec//60
    sec = sec%60
    return str(mins)+":"+str(sec//10)+str(sec%10)+"."+str(tenthSec)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global stops, score
    if timer.is_running():
        timer.stop()
        stops = stops + 1
        if (time%10 == 0):
            score = score + 1
    
def reset():
    global time,stops,score
    timer.stop()
    time = 0
    stops = 0
    score = 0
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time = time + 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time),[45,115],42,"White")
    canvas.draw_text(str(score)+"/"+str(stops),[145,40],30,"Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100,time_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()