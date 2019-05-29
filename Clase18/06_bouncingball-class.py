import stddraw
import ball

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

bola = ball.Ball(.480, .860, .015, .023, .05, stddraw.BLACK)

while True:
    # update velocity
    bola.update()
    # clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)
    
    # draw the ball on the screen
    bola.draw()
    
    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)
