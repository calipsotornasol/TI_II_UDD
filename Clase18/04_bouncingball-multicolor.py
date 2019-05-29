import stddraw
from color import Color
from random import randrange

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

radius = .05

rx = .480
ry = .860
vx = .015
vy = .023

while True:
    # Bounce of wall according to elastic collition
    # update velocity
    if abs(rx + vx) + radius > 1.0:
        vx = -vx
    if abs(ry + vy) + radius > 1.0:
        vy = -vy
    
    # Update position
    rx = rx + vx
    ry = ry + vy
    
    # Clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)
    
    # Generate random color
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    c = Color(r, g, b)
    
    # Draw the ball on the screen
    stddraw.setPenColor(c)
    stddraw.filledCircle(rx, ry, radius)
    
    # Copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)
