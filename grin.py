from turtle import *

speed(0)

def grin():
    fillcolor("yellow")
    begin_fill()
    circle(30)
    end_fill()
    
    color("black")
    penup()
    left(90)
    forward(35)
    left(90)
    forward(10)
    right(180)
    pendown()
    
    begin_fill()
    circle(5)
    end_fill()
    
    penup()
    forward(20)
    pendown()
    
    begin_fill()
    circle(5)
    end_fill()
    
    penup()
    right(90)
    forward(10)
    pendown()
    
    fillcolor("white")
    begin_fill()
    for i in range(2):
        forward(10)
        right(90)
        forward(20)
        right(90)
    end_fill()
    

    forward(5)
    right(90)
    forward(20)
    right(90)
    forward(5)
    right(90)
    forward(5)
    right(90)
    forward(10)
    left(90)
    forward(5)

    left(90)
    forward(10)
    right(90)
    forward(5)  
    right(90)
    forward(10)
    
    penup()
    forward(15)
    right(90)
    forward(15)
    right(180)
    forward(10)
    pendown()
grin()
done()