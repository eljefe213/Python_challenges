from turtle import *
speed(5)
width(5)

color('red', 'yellow') # Two inputs: a stroke color and a fill color.

begin_fill() # Start of a filled shape.
for i in range(5): # Repeat 5 times
    # The turning angle is chosen so that the star closes in on itself after five turns.
    right(180 - 36) # Turning angle 
    forward(200)
end_fill() # Fills in the shape it has been drawing
    
hideturtle()
bye()
