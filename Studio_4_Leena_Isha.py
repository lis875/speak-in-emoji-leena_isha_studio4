from turtle import*
import turtle
wn = Screen()
speed(0)
def surprised():
    fillcolor("yellow")
    begin_fill()
    left(90)
    circle(30)
    right(90)
    end_fill()
    penup()
    back(15); left(180);
    right(90)
    forward(10)
    left(90)
    forward(5)
    pendown()
    fillcolor("black")
    begin_fill()
    circle(5)
    end_fill()
    penup(); 
    forward(20)
    fillcolor("black")
    begin_fill()
    circle(5.5)
    end_fill()
    penup()
    left(90)
    forward(35) 
    left(90)
    forward(13)
    pendown()
    fillcolor("white")
    begin_fill()
    circle(9)
    end_fill()

def move_next():
    penup()
    forward(100)
    pendown()

def sleepy():
    surprised()
    penup()
    forward(10)
    pendown()
    turtle.color('Black')
    turtle.write("Z Z Z", font = ('Arial', 10, 'bold'))


surprised()
move_next()
sleepy()


done()