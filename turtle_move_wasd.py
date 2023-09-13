import turtle

def turtle_move_w():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)

def turtle_move_a():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)
    
def turtle_move_s():
    turtle.setheading(-90)
    turtle.stamp()
    turtle.forward(50)
    
def turtle_move_d():
    turtle.setheading(0)
    turtle.stamp()
    turtle.forward(50)

def turtle_reset():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(turtle_move_w,'w')
turtle.onkey(turtle_move_a,'a')
turtle.onkey(turtle_move_s,'s')
turtle.onkey(turtle_move_d,'d')
turtle.onkey(turtle_reset,'Escape')
turtle.listen()
