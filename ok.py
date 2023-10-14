from turtle import *

speed(0)

def ok():
    fillcolor("yellow")
    begin_fill()
    circle(30)
    end_fill()
    
    color("black")
    penup()
    left(90)
    forward(35)
    left(90)
    forward(15)
    right(180)
    pendown()
    
    forward(15)
    penup()
    forward(5)
    pendown()
    forward(15)
    
    penup()
    right(90)
    forward(15)
    right(90)
    forward(10)
    pendown()
    forward(20)
    
    penup()
    left(90)
    forward(20)
    left(90)
    forward(10)
    

ok()
done()