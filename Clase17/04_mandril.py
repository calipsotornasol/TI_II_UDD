import sys
import stddraw
import luminance
from picture import Picture

pic = Picture(sys.argv[1])

for col in range(pic.width()):
    for row in range(pic.height()):
        #print(pic.get(col, row))
        pic.set(col, row, pic.get(col, row))

stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show()
