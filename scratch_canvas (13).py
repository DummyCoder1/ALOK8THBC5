import turtle

import turtle

turtle.shape('turtle')
turtle.pencolor('blue')
for x in range(0, 20):
    turtle.forward(100)
    if x%2==0:
        turtle.left(225)
    else:
        turtle.left(175)


