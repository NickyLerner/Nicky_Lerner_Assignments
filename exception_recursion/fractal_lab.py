import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor('white')
my_turtle.width(4)
my_turtle.speed(0)
my_turtle.shape("turtle")


# Turtle Recursion (25pts)

# 1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (10pts)


def h_fractal(x, y, height, width, depth):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    my_turtle.goto(x - (width/2), y)
    my_turtle.goto(x - (width/2), y + (height/2))
    pos1 = my_turtle.pos()
    my_turtle.goto(x - (width/2), y - (height/2))
    pos2 = my_turtle.pos()
    my_turtle.goto(x - (width/2), y)
    my_turtle.goto(x + (width/2), y)
    my_turtle.goto(x + (width/2), y + (height/2))
    pos3 = my_turtle.pos()
    my_turtle.goto(x + (width/2), y - (height/2))
    pos4 = my_turtle.pos()
    if depth > 0:
        h_fractal(pos1[0], pos1[1], height // 2, width // 2, depth - 1)
        h_fractal(pos2[0], pos2[1], height // 2, width // 2, depth - 1)
        h_fractal(pos3[0], pos3[1], height // 2, width // 2, depth - 1)
        h_fractal(pos4[0], pos4[1], height // 2, width // 2, depth - 1)


h_fractal(0, 0, 300, 250, 4)

my_turtle.color('red')
# 2)  Using the turtle library, create any of the other recursive patterns in the data folder.
#  Challenge yourself to match your pattern as closely as you can to the image.  (10pts)
#  Note:  The Koch snowflake shows step by step building of the fractal.  
#  The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)


def snowflake(x, y, length, depth):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    for i in range(6):
        if depth > 0:
            my_turtle.forward(length/2)
            position = my_turtle.pos()
            snowflake(position[0], position[1], length/3, depth - 1)
            my_turtle.right(60)
        my_turtle.goto(x, y)


def another_triangle(length, depth):
    my_turtle.left(60)
    my_turtle.forward(length/3)
    if depth > 0:
        # my_turtle.left(60)
        another_triangle(length/3, depth-1)
        my_turtle.right(60)
        my_turtle.forward(length/3)
    else:
        my_turtle.forward(length/3)
    my_turtle.forward(length/3)
    my_turtle.right(120)
    my_turtle.forward(length/3)
    if depth > 0:
        # my_turtle.left(60)
        another_triangle(length/3, depth-1)
        my_turtle.right(60)
        my_turtle.forward(length/3)
    else:
        my_turtle.forward(length/3)
    my_turtle.forward(length/3)
    my_turtle.left(60)


def triangle_flake(x, y, length, depth):
    my_turtle.up()
    my_turtle.goto(x, y + (length/2))
    my_turtle.down()
    my_turtle.right(60)
    my_turtle.forward(length/3)
    if depth > 0:
        another_triangle(length/3, depth - 1)
    else:
        my_turtle.forward(length/3)
    my_turtle.forward(length/3)
    my_turtle.right(120)
    my_turtle.forward(length/3)
    if depth > 0:
        another_triangle(length/3, depth - 1)
    else:
        my_turtle.forward(length/3)
    my_turtle.forward(length/3)
    my_turtle.right(120)
    my_turtle.forward(length/3)
    if depth > 0:
        another_triangle(length/3, depth - 1)
    else:
        my_turtle.forward(length/3)
    my_turtle.forward(length/3)


# snowflake(0, 0, 400, 4)
# triangle_flake(0, 0, 400, 2)

# 3)  Create your own work of recursive art with a repeating pattern of your making.
#  It must be a repeated pattern using recursion (not just loops). Snowflakes, trees, and spirals are a common choice.  
#  Play around and have fun with it.  (5pt) 
my_turtle.color('blue')


def triangle_upon_triangle(x, y, length, depth):  # We can say that this is the fractal I made myself.
    my_turtle.up()
    my_turtle.goto(x, y)
    if depth % 2 == 0:
        my_turtle.goto(x, y - (length/2))
        my_turtle.down()
        pos1 = my_turtle.pos()
        my_turtle.goto(x - (length/2), y + (length/2))
        pos2 = my_turtle.pos()
        my_turtle.goto(x + (length/2), y + (length/2))
        pos3 = my_turtle.pos()
        my_turtle.goto(x, y - (length/2))
    elif depth % 2 == 1:
        my_turtle.goto(x, y + (length/2))
        my_turtle.down()
        pos1 = my_turtle.pos()
        my_turtle.goto(x - (length/2), y - (length/2))
        pos2 = my_turtle.pos()
        my_turtle.goto(x + (length/2), y - (length/2))
        pos3 = my_turtle.pos()
        my_turtle.goto(x, y + (length/2))
    if depth > 0:
        triangle_upon_triangle(pos1[0], pos1[1], length // 3, depth - 1)
        triangle_upon_triangle(pos2[0], pos2[1], length // 3, depth - 1)
        triangle_upon_triangle(pos3[0], pos3[1], length // 3, depth - 1)


triangle_upon_triangle(0, 0, 300, 5)

#  General expectations for all problems
#  Give all your fractals a depth of at least 4.  (Don't make programs that take forever though)  
#  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
#  All three recursive drawings can be on the same program.  Just use screen.clear() between problems.
#  Alternately, you could draw to three different screen objects.
#  Run your turtles at max speed.
#  Have fun!
 
#  Resource to help you out >>> https://docs.python.org/3.3/library/turtle

my_screen.exitonclick()

