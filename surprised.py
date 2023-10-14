from turtle import *

speed(0)

def surprised():
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
    right(90)
    forward(10)
    pendown()
    fillcolor("white")
    begin_fill()
    circle(9)
    end_fill()
    
    penup()
    left(90)
    forward(25)
    left(90)
    
surprised()
done()