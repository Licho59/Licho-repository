# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:37:09 2017

@author: Leszek
"""
# Testing of Turtle module
import turtle
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Tess & Alex')

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(5)

alex = turtle.Turtle()

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(120)

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()


