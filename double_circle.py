from turtle import *

width(2)

# Function definition 
def circle(size): # Argument added in parentheses
    penup()
    forward(200)
    pendown()
    left(90)
    for i in range(60):
        forward(size) # Argument used in the program
        left(6)
    right(90)
    penup()
    back(200)
    pendown()

# Function calls
# Draws a circle with size of 10
circle(10) # Argument size replaced with 10 everywhere

# Draws a circle with size of 20
circle(20) # Argument size replaced with 20 everywhere

bye()