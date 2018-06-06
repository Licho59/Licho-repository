'''Using the turtle graphics module, write a recursive program to display a Koch snowflake.'''

import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)
        
           
t = turtle.Turtle()
t.penup()
t.goto(-300, 150)
t.pendown()
myWin = turtle.Screen()
t.pensize(4)
t.color('pink')
t.speed(10)

for i in range(3):
    koch(t, 5, 400)
    t.right(120)

myWin.exitonclick()           
