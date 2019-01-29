import turtle
import random

def simpleTree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        simpleTree(branchLen - 15, t)
        t.left(40)
        simpleTree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)


def tree(branchLen, t, m, c):
    if branchLen > 5:
        if branchLen < 20:
            c = "green yellow"
            t.color(c)
        t.forward(branchLen)
        t.right(20)
        m -= 0.4
        t.pensize(m)
        l = random.randint(2, 20)
        tree(branchLen - l, t, m, c)
        if branchLen < 20:
            c = "green yellow"
            t.color(c)
        t.left(40)
        m -= 0.5
        t.pensize(m)
        tree(branchLen - l, t, m, c)
        t.right(20)
        t.backward(branchLen)
        t.color("green")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(130)
    t.down()
    #t.color("green")
    #t.pensize(5)
    #simpleTree(75, t)
    m = 10
    t.pensize(m)
    c = "green"
    t.color(c)
    tree(100, t, m, c)
    t.speed(10)
    myWin.exitonclick()


main()

