from turtle import Turtle, Screen
import random
import time

COLORS = ["red", "blue", "green", "yellow", "black", "purple"]
INITIAL_VERTICAL_COORDS = [(-200, -280), (-100, -280), (0, -280), (100, -280), (200, -280), ]
INITIAL_HORIZONTAL_COORDS = [(-280, 200), (-280, 100), (-280, 0), (-280, -100), (-280, -200), ]

vertical_turtles = []
horizontal_turtles = []
collisions = 0
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)


# set up the turtle lists
def initiate_turtles():
    for i in range(0, 5):
        vt = Turtle("turtle")
        vt.color(random.choice(COLORS))
        vt.setheading(90)
        vt.penup()
        vt.goto(INITIAL_VERTICAL_COORDS[i])
        vertical_turtles.append(vt)

        ht = Turtle("turtle")
        ht.color(random.choice(COLORS))
        ht.setheading(0)
        ht.penup()
        ht.goto(INITIAL_HORIZONTAL_COORDS[i])
        horizontal_turtles.append(ht)


def move_turtles():
    for i in range(0, 5):
        vertical_turtles[i].forward(random.randint(1, 10))
        horizontal_turtles[i].forward(random.randint(1, 10))


# check if a vertical/horizontal turtle hit
def check_collisions():
    global collisions
    for vt in vertical_turtles:
        for ht in horizontal_turtles:
            if vt.distance(ht) < 10:
                collisions += 1
                print(collisions)

# reset to initial positions if they go off the screen
def reset_turtles():
    for i in range(0, 5):
        if vertical_turtles[i].ycor() > 300:
            vertical_turtles[i].goto(vertical_turtles[i].xcor(), -300)
        if horizontal_turtles[i].xcor() > 300:
            horizontal_turtles[i].goto(-300, horizontal_turtles[i].ycor())


initiate_turtles()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    move_turtles()
    check_collisions()
    reset_turtles()

screen.exitonclick()
