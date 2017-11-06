#ALL TOGETHER- DESIGN PROJECT
import turtle
qwe = turtle.Turtle()
qwe.speed(11)
turtle.colormode(255)
from random import*

from myfunctions_Carlos import*

turtle.bgcolor(0,0,0)#sky_color
for times in range(100):#stars
    star(qwe)
    jump(qwe,randint(-1000,1000),randint(30,500)) 
jump(qwe,300,350)
qwe.right(90)
qwe.color(200,200,200)#moon
qwe.begin_fill()
qwe.circle(90)
qwe.end_fill()
qwe.penup()
qwe.forward(35)
qwe.left(90)
qwe.forward(45)
qwe.pendown()
qwe.color(0,0,0)
qwe.begin_fill()
qwe.circle(80)
qwe.end_fill()
jump(qwe,0,0)
qwe.color(155,239,242)#mountains
qwe.right(120)
qwe.begin_fill()
qwe.forward(830)
qwe.right(180)
qwe.forward(1670)
qwe.right(120)
qwe.forward(300)
qwe.right(100)
qwe.forward(246)
qwe.left(90)
qwe.forward(315)
qwe.right(70)
qwe.forward(100)
qwe.left(45)
qwe.forward(40)
qwe.right(100)
qwe.forward(175)
qwe.left(100)
qwe.forward(100)
qwe.right(90)
qwe.forward(40)
qwe.left(120)
qwe.forward(200)
qwe.right(100)
qwe.forward(80)
qwe.left(90)
qwe.forward(50)
qwe.right(75)
qwe.forward(300)
qwe.left(90)
qwe.forward(200)
qwe.right(100)
qwe.forward(380)
qwe.right(50)
qwe.forward(85)
qwe.end_fill()
qwe.width(3)
jump(qwe,0,0)
qwe.right(90)
for times in range(155):#water
    qwe.color(155-times,239-times,242-times)
    qwe.forward(1000)
    qwe.right(180)
    qwe.forward(2000)
    jump(qwe,0,0-times)
jump(qwe,0,-155)
for times in range(82):
    qwe.color(0,83-times,86-times)
    qwe.forward(1000)
    qwe.right(180)
    qwe.forward(2000)
    jump(qwe,0,-155-times)
qwe.width(2)
jump(qwe,0,0)
for times in range(300):#water ripple
    water_ripple(qwe)
    jump(qwe,randint(-800,800),randint(-300,0))
jump(qwe,300,-350)
qwe.color(200,200,200)
for times in range(20):#300_350
    moon_reflection(qwe)
    jump(qwe,randint(250,350),randint(-400,-300))

    





