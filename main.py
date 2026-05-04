from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key):
        super().__init__()
        self.health = 3
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.color = color
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())

    def fire(self):
        self.bullets.append(Bullet(self))


class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color(player.color)
        self.setheading(player.heading())
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.st()


screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()


playing_area()

p1 = Player(-100, 0, "red",screen, "d", "a","w","s")
p2 = Player(100,0,"blue",screen, "Right","Left","up","down")

while p1.alive and p2.alive:
    p1.move()
    p2.move()

    for obj in turtles:
        move_heading(obj, turtles)
        if player!= None and player.distance(obj) < 20:
            obj.hideturtle()
            turtles.remove(obj)
            turtle.health-=1

    for bullet in turtles:
        move_heading(bullet, turtles)
        if player.health==2 and player.distance(bullet) < 20:
            turtle.color("yellow")
        elif player.health==2 and player.distance(bullet) < 20:
            turtle.color("red")
        elif player.health==1 and player.distance(bullet) < 20:
            turtle.color("red")
        else:
            obj.hideturtle()
            turtles.remove(bullet)

# def detect_bullets(p1,p2):
#     if p1!= None and bullets.distance(obj)<20:
#         p1.color("yellow") 
#     elif p1.distance==bullets.distance and p1.color==yellow:
#         p1.color("red")
#     else:

# if

screen.exitonclick()