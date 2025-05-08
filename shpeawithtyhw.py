import turtle
turtle.Screen().bgcolor("red")

board = turtle.Turtle()

#Triangle

board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

#Square
board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

#Rectangle

board.forward(200)
board.left(90)

board.forward(100)
board.left(90)

board.forward(200)
board.left(90)

board.forward(100)
board.left(90)

board.done()