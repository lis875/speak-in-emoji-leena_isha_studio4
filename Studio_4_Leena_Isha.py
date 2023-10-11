from turtle import*
speed(0)
def happy_smiley():
    fillcolor("yellow")
    begin_fill()
    left(90)
    circle(30)
    right(90)
    end_fill()
    penup()
    back(15); left(90); forward(10)
    
    pendown()
    fillcolor("black")
    begin_fill()
    circle(5)
    end_fill()
    penup(); 
    left(90); 
    forward(25)
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
    penup()
    forward(20)
    





happy_smiley()

done()