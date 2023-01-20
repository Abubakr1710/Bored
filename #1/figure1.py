import turtle as t # import turtle module
import colorsys as cs # import colorsys module
t.setup(800, 800) # set the window size
t.speed(0) # set the drawing speed
t.tracer(10) # set the drawing speed
t.width(2) # set the pen width
t.bgcolor("black") # set the background color
for j in range(25):
    for i in range(15):
        t.color(cs.hsv_to_rgb(i/15, j/25, 1)) # set the pen color
        t.right(90) # turn right 90 degrees
        t.circle(200 - j*4, 90) # draw a circle
        t.left(90) # turn left 90 degrees
        t.circle(200 - j*4, 90) # draw a circle
        t.right(180) # turn right 180 degrees
        t.circle(50,24) # draw a circle
t.hideturtle() # hide the turtle
t.done() # keep the window open