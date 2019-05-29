import stddraw
from ball import Ball

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

balls = [
    Ball(.480, .860, .015, .023, .05, stddraw.BLACK),
    Ball(.480, .860, .030, .046, .05, stddraw.BLUE),
    Ball(.180, .260, .040, .026, .05, stddraw.GREEN)
]

while True:
    # Update velocity
    for b in balls:
        b.update()
    
    # Clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)
    
    # Draw the ball on the screen
    for b in balls:
        b.draw()
    
    # Copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)
