from turtle import *
import turtle


def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            #forward(a / 3)
            koch(a / 3, order - 1)
            left(t)
    else:
        forward(a)

#koch(100,1)


# Choose colours and size
color("sky blue", "white")
bgcolor("red")
size = 400
order = 7

penup()
backward(size/1.732)
left(30)
pendown()

# Make it fast
tracer(100)
hideturtle()

begin_fill()

for i in range(3):
    koch(size, order)
    right(120)

end_fill()

# Make the last parts appear
update()

turtle.done()
