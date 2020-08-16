# Python program that uses turtles, loops and has at least one user-defined function in it 
# to help draw things

# initials program 
from turtle import *

def drawSquare():
    for i in range(4):
        forward(50)
        right(90)
        
def drawTurtle():
    for i in range(60):
        drawSquare()
        right(6)

drawTurtle()



