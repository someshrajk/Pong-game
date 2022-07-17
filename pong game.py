import turtle

#Screen

screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width =1000 , height =600)

#Left paddle
left_pad =turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6,stretch_len=2)
left_pad.penup()
left_pad.goto(-400,0)


#Right paddle
right_pad =turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6,stretch_len=2)
right_pad.penup()
right_pad.goto(400,0)

#Ball

ball = turtle.Turtle()
ball.shape("circle")
ball.speed(40)
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx =5
ball.dy =-5

#Score

Left_Player =0
Right_Player=0

#Display

sketch =turtle.Turtle()
sketch.speed(0)
sketch.color("grey")
sketch.penup()
sketch.hideturtle()
sketch.goto(0,260)
sketch.write("Player_1 : 0 Player_2 : 0",align="center",font=("copperplate",15,"bold"))

#Move Functions

def padup():
    y = left_pad.ycor()
    y+= 20
    left_pad.sety(y)


def paddown():
    y = right_pad.ycor()
    y-= 20
    left_pad.sety(y)
    

def padaup():
    y = right_pad.xcor()
    y+= 20
    right_pad.sety(y)


def padadown():
    y = right_pad.ycor()
    y-= 20
    right_pad.sety(y)

# keyboard Settings

screen.listen()
screen.onkeypress(padup, "s")
screen.onkeypress(paddown, "d")
screen.onkeypress(padaup, "Up")
screen.onkeypress(padadown, "Down")

while True:
    screen.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
#Border
    
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0,0)
        ball.dy *= -1
        Left_Player += 1
        sketch.clear()
        sketch.write("Player_1 : {} Player_2 : {}".format(Left_Player,Right_Player),align="center",font=("copperplate",15,"bold"))

    if ball.xcor() < -500:
        ball.goto(0,0)
        ball.dy *= -1
        Right_Player += 1
        sketch.clear()
        sketch.write("Player_1 : {} Player_2 : {}".format(Left_Player,Right_Player),align="right",font=("copperplate",15,"bold"))
        
    #Ball Colision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < right_pad.ycor()+40 and ball.ycor() > right_pad.ycor()-40):
        ball.setx(360)
        ball.dx *= -1
        
    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < left_pad.ycor()+40 and ball.ycor() > left_pad.ycor()-40):
        ball.setx(-360)
        ball.dx *= -1
        

       








    
