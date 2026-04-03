import turtle
r=65
xy_list=[(-150,25),(0,25),(150,25),(-75,-45),(75,-45)]
color_list=['blue','black','red','yellow','green']
turtle.pensize(8)
turtle.speed(100)
for i in range(5):
    turtle.penup()
    turtle.goto(xy_list[i][0],xy_list[i][1])
    turtle.pendown()
    turtle.color(color_list[i])
    turtle.circle(r)
    turtle.hideturtle()
turtle.done()