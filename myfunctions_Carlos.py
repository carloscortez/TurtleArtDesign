#carlos
#myfunctions
def square(t,d):
    for times in range(4):
        t.forward(d)
        t.right(90)
def triangle(t,d):
    for times in range(3):
        t.forward(d)
        t.right(120)
def polygon(t,s,d):
     angle = 360/s
     t.begin_fill()
     for times in range(s):
         t.forward(d)
         t.right(angle)
     t.end_fill()    
def jump(t,x,y):
     t.penup()
     t.goto(x,y)
     t.pendown()
def cool(t,d,c1,c2):
     t.color(c1)
     polygon(t,4,d)
     t.color(c2)
     polygon(t,3,d)

#STAR FUNCTION FOR BACKGROUND
#COLOR FOR STARS - 247,290,213
def star(t):
    t.begin_fill()
    for times in range(4):
        t.color(247,209,213)
        t.forward(8)
        t.right(150)
    t.end_fill()
        
def moon_reflection(t):
    t.color(200,200,200)
    t.forward(90)
def water_ripple(t):
    t.color(0,0,0)
    t.forward(90)
    t.right(180)
    t.forward(180)
