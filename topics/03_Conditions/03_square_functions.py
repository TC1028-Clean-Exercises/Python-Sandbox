"""
Drawing squares using Turtle
Using functions to improve the program

Gilberto Echeverria
2021-08-25
"""

import turtle


# DEFINE a function to draw a square
def draw_square(size, my_color, fill):
    """ Drawing a colored square """
    # Change the color
    turtle.color(my_color)
    # Fill the square if the 3rd argument is True
    if fill:
        turtle.begin_fill()
    # Draw the shape
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    if fill:
        turtle.end_fill()


def go_to_position(x, y):
    """ Move to a different position, without drawing along the way """
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()


def main():
    """ Starting point for the program """
    # CALL the functions defined previously
    go_to_position(200, 100)
    draw_square(200, "red", True)
    go_to_position(-100, -300)
    draw_square(200, "green", False)
    go_to_position(-400, 100)
    draw_square(200, "blue", True)
    turtle.done()


# Make sure the 'main' function is called to start the program
if __name__ == "__main__":
    main()
