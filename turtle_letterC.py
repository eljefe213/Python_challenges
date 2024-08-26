from turtle import *
width(5)

left(180)

forward(50)
left(45)    # Turning angle
forward(50) 
left(45)    # Turning angle
forward(50)
left(45)    # Turning angle
forward(50) 
left(45)    # Turning angle
forward(50) 

hideturtle()
bye()


# The same program with the for loop 

from turtle import *
width(5)

left(180)

# Start of for loop.
for i in range(5):
    forward(50) 
    left(45) 
hideturtle()
bye()
