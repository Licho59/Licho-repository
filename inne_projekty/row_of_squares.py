# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:53:17 2017

@author: Leszek
"""
import turtle

def make_window(colr, ttle):
    '''Set up the window with given background color and title.
    '''
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    '''Set up a turtle with the given color and pensize.
    Returns the new turtle.
    '''
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_square(t, size, angle):
    for i in range(4):
        t.forward(size)
        t.left(angle)
        

wn = make_window('lightgreen', 'Row of squares')
tess = make_turtle('magenta', 3)
size = 20
angle = 90

for i in range(5):
    draw_square(tess, size, angle)
    tess.penup()
    tess.forward(size * 2)
    tess.pendown()
    
wn.mainloop()
wn.exitonclick()
    
    