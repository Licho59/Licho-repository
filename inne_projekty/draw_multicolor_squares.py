# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:37:09 2017

@author: Leszek
"""
# Testing of Turtle module
import turtle
__import__("turtle").__traceable__ = False


def draw_multicolor_square(t, sz):
    '''Make turtle t draw a multi-color square of sz length'''
    draw_rectangle(t, sz, sz)
    
    for i in ['red', 'pink', 'hotpink', 'blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)
        
def draw_rectangle(t, w, h):
    '''Get turtle t to draw a rectangle of width w and height h.'''
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        
wn = turtle. Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range(15):
    draw_multicolor_square(tess, size)
    size += 10
    tess.forward(10)
    tess.right(18)  

wn.mainloop()
wn.exitonclick()
#turtle.clear()
