# Importing relevant modules
import turtle
import time

# setting up a turtle
win = turtle.Screen()
win.setup(width=1000, height=800)
win.bgcolor("black")


def spash_title():
    title_content = [
        "Python Project", "Scorpious Constellation", "Jigmey Gurung"
    ]
    for i in title_content:
        turtle.write(i, False, align="center", font=("Courier", 20, "normal"))
        turtle.forward(100)

# First Page
def splash():
    turtle.pencolor("white")
    turtle.penup()
    turtle.hideturtle()
    turtle.right(90)
    spash_title()
    time.sleep(3)


# Second Page
def scorpious():
    win.clearscreen()
    win.addshape("scorpius.gif")

    t = turtle.Turtle()
    t.shape("scorpius.gif")
    time.sleep(3)


# Fourth Page
def constellation():
    turtle.clearscreen()
    win.bgpic("space.gif")
    turtle.hideturtle()

    # Positions for my dots using (x,y) co-ordinates
    # List of 17 co-ordinates
    coordinates = [(-295, -110), (-240, -100), (-270, -140), (-285, -160),
                   (-250, -200), (-160, -205), (-120, -190), (-100, -115),
                   (-90, -60), (-50, 30), (-30, 40), (-10, 50), (60, 80),
                   (55, 115), (15, 130), (48, 35), (55, 0)]

    # Iterate through the co-ordinates and call make_dot functions  to create dots
    for i in coordinates:
        turtle.penup()
        turtle.setpos(i)
        turtle.pendown()
        turtle.speed(1)
        make_dots()

    # Connect the dots and setting co-ordinates[0] as the starting point
    my = turtle.Turtle()
    my.hideturtle()
    my.penup()
    my.speed(1)
    my.pensize(2)
    for i in coordinates:
        my.goto(i)
        my.color("white")
        my.pendown()
        # Once the dots get connected to 14
        # lift the pen up and set it to 12 and continue to connect co-orinates[12] to [15] and so on
        if (i == coordinates[14]):
            my.penup()
            my.goto(coordinates[12])
            my.pendown()
            continue


# Create dots
def make_dots():
    turtle.color("orange")
    turtle.pendown()
    turtle.dot(12)


# Third Page
def thirdPage():
    win.clearscreen()
    turtle.bgcolor('black')
    turtle.color('white')
    turtle.speed(1)

    turtle.penup()
    turtle.goto(-200, 250)
    turtle.write("The Scorpious Constellation",
                 font=("Courier", 14, 'italic', 'bold'))
    turtle.penup()
    turtle.goto(-250, -110)
    turtle.pendown()

    turtle.dot(12)
    turtle.left(10)
    turtle.forward(50)
    turtle.write("  Shaula")
    turtle.dot(15)

    turtle.right(25)
    turtle.forward(20)
    turtle.write("      Lesath")
    turtle.dot(12)

    turtle.right(110)
    turtle.forward(40)
    turtle.dot(14)

    turtle.left(20)
    turtle.forward(20)
    turtle.dot(12)

    turtle.left(60)
    turtle.forward(40)
    turtle.write("     Sargas")
    turtle.dot(16)

    turtle.left(50)
    turtle.forward(70)
    turtle.dot(12)

    turtle.left(20)
    turtle.forward(40)
    turtle.dot(10)

    turtle.left(68)
    turtle.forward(55)
    turtle.dot(12)

    turtle.left(3)
    turtle.forward(45)
    turtle.dot(14)

    turtle.right(25)
    turtle.forward(100)
    turtle.write("      Antares")
    turtle.dot(12)

    turtle.right(10)
    turtle.forward(30)
    turtle.dot(20)

    turtle.right(15)
    turtle.forward(30)
    turtle.write("     Alniyat")
    turtle.dot(14)

    turtle.right(0)
    turtle.forward(80)
    turtle.write("     Dschubba")
    turtle.dot(20)

    turtle.left(60)
    turtle.forward(40)
    turtle.write("     Graffias")
    turtle.dot(14)

    turtle.left(60)
    turtle.forward(30)
    turtle.dot(10)
    turtle.penup()
    turtle.back(30)
    turtle.right(45)
    turtle.back(40)
    turtle.pendown()

    turtle.left(150)
    turtle.forward(50)
    turtle.dot(15)

    turtle.left(2)
    turtle.forward(40)
    turtle.dot(10)
    turtle.penup()

    time.sleep(3)


splash()
scorpious()
thirdPage()
constellation()

turtle.done()
