import turtle

def draw_art():
    bg = turtle.Screen()
    bg.bgcolor('white')

    # draw a square
    '''ken = turtle.Turtle() # create first turtle
    ken.shape("turtle")
    ken.color('pink')
    ken.speed(2)
    draw_square(ken)

    # darw a circle
    john = turtle.Turtle() # create second turtle
    john.shape('arrow')
    john.color('red')
    john.circle(100)'''

    #
    
    mary = turtle.Turtle()
    mary.shape('turtle')
    mary.color('blue')
    mary.pencolor('black')
    mary.speed(10)
    bigone(mary)

    '''
    for i in range(1, 37):
        draw_triangle(mary)
        mary.right(10)
  
    '''
    
    bg.exitonclick() # function to exit by click

def draw_square(turlte_name):
    for i in range(1,5):     
        turlte_name.forward(100)
        turlte_name.right(90)
'''    
def draw_triangle(john):
    john.forward(45)
    john.left(100)
    john.forward(150)
    john.left(160)
    john.forward(150)
    john.left(100)
    john.forward(45)
'''

def draw_triangle(ken):
    ken.begin_fill()
    for i in range(1,4):
        ken.forward(50)
        ken.left(120)
    ken.end_fill()

def big_triangle(mary):
    for i in range(1, 5):
        draw_triangle(mary)
        mary.forward(50)
    mary.left(120)
    mary.forward(50)
    for i in range(1, 4):
        draw_triangle(mary)
        mary.forward(50)
    mary.left(120)
    for i in range(1, 3):
        mary.forward(50)
        draw_triangle(mary)

def bigone(mary):
    big_triangle(mary)
    mary.forward(300)
    mary.left(120)
    big_triangle(mary)
    mary.backward(100)
    mary.right(60)
    mary.backward(200)
    mary.left(60)
    big_triangle(mary)

draw_art()
