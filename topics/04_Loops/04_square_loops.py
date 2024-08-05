"""
Drawing various polygons using Turtle
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


def draw_polygon(sides, size, color, fill):
    """ Draw any polygon of the number of sides specified """
    # Change the color
    turtle.color(color)
    # Fill the square if the 3rd argument is True
    if fill:
        turtle.begin_fill()
    # Draw the shape
    angle = 360 / sides
    count = 0
    while count < sides:
        turtle.forward(size)
        turtle.left(angle)
        count += 1
    if fill:
        turtle.end_fill()


def go_to_position(x, y):
    """ Move to a different position, without drawing along the way """
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()


def main():
    """ Starting point for the program """
    # Initialize the values for the sequence of squares
    pos_x = -400
    size = 160
    col = 0
    while col < 4:
        # Start one row of squares
        go_to_position(pos_x + 200 * col, 200)
        draw_square(size, "red", True)

        # Another row of shapes
        go_to_position(pos_x + 200 * col, 0)
        draw_polygon(6, 80, "green", True)

        # Another row of shapes
        go_to_position(pos_x + 200 * col, -200)
        draw_polygon(12, 40, "blue", True)

        col += 1
    # Let the window remain open
    turtle.done()


# Make sure the 'main' function is called to start the program
if __name__ == "__main__":
    main()
