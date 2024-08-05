"""
Simple program to draw a square using Turtle

Gilberto Echeverria
2021-08-23
"""

import turtle


# Draw a single square
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)

# Move to a different position
# Raise the pen, so we don't draw as we move
turtle.up()
turtle.setposition(-400, -400)
# Lower the pen to start drawing again
turtle.down()

# Another square
turtle.begin_fill()
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.end_fill()

# Move to a different position
turtle.up()
turtle.setposition(-800, 0)
turtle.down()

# Another square
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)

# Move to a different position
turtle.up()
turtle.setposition(400, -400)
turtle.down()

# Another square
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)


# Finish and wait for the window to be closed
turtle.done()
