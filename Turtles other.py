import turtle

def fractal(t, level, dist):
    if level == 0:
        t.down()
        t.begin_fill()
        for _ in range(3):
            t.forward(dist)
            t.left(120)
        t.end_fill()
        t.up()
    else:
        fractal(t, level-1, dist/2)
        t.forward(dist)
        t.left(120)
        fractal(t, level-1, dist/2)
        t.forward(dist)
        t.left(120)
        fractal(t, level-1, dist/2)
        t.forward(dist)
        t.left(120)

window = turtle.Screen()
window.screensize(300,300,"black")
window.setworldcoordinates(0,0,300,300)

terry = turtle.Turtle()
terry.speed(0)
terry.color("black", "purple")
fractal(terry, 2, 50)

window.exitonclick()
