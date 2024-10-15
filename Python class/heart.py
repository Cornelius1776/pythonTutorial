import turtle
from turtle import *

wn = Screen()
wn.bgcolor('black')
t = turtle.Turtle()
t.pencolor('white')


def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)


def draw_heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()


draw_heart()
t.ht()


def write_up(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.color('white')
    style = ('Roboto', 20, 'italic')
    t.write(message, font=style)


write_up('I', (-68, 95))
write_up('L', (-57, 95))
write_up('O', (-46, 95))
write_up('V', (-30, 95))
write_up('E', (-14, 95))
write_up('Y', (10, 95))
write_up('O', (26, 95))
write_up('U', (45, 95))

wn.mainloop()
