import turtle

# Define screen size and colors
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# Define the left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

#Define the ball
ball = turtle.Turtle()
ball.color("blue")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -1

#define the right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

#Define text
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player One: 0  Player Two: 0", align="center", font=("Courier", 20, "normal"))

#Paddle movement functions
def left_paddle_up():
    y = left_paddle.ycor()
    y += 30
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 30
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 30
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 30
    right_paddle.sety(y)

def main():
   
    #Set base score
    score_player_one = 0
    score_player_two = 0

    #Keep looping - not the cleanest way to do this, but it is all I could come up with.
    while True: 

        screen.update()
        screen.listen()
        screen.onkeypress(left_paddle_up, "w")
        screen.onkeypress(left_paddle_down, "s")
        screen.onkeypress(right_paddle_up, "Up")
        screen.onkeypress(right_paddle_down, "Down")
        
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        
        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *= -1

        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1

        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
            score_player_one += 1
            if score_player_one == 10:
                pen.clear()
                pen.write("Well Done Player One", align="center", font=("Courier", 20, "normal"))
                turtle.done()
               
            pen.clear()
            pen.write("Player One: {} Player Two: {}".format(score_player_one, score_player_two), align="center", font=("Courier", 20, "normal"))
        if ball.xcor() > 380:
            score_player_one
            pen.clear()
            pen.write("Player One: {} Player Two: {}".format(score_player_one, score_player_two), align="center", font=("Courier", 20, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        if (ball.xcor() > 340 and ball.xcor() < 350) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
            score_player_two += 1
            if score_player_two == 10:
                pen.clear()
                pen.write("Well Done Player Two", align="center", font=("Courier", 20, "normal"))
                turtle.done()
                
            pen.clear()
            pen.write("Player One: {} Player Two: {}".format(score_player_one, score_player_two), align="center", font=("Courier", 20, "normal"))
        if ball.xcor() < -380:
            score_player_two = 0
            pen.clear()
            pen.write("Player One: {} Player Two: {}".format(score_player_one, score_player_two), align="center", font=("Courier", 20, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
        
        if (ball.xcor() > 340 and ball.xcor() < 350) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
       
if __name__ == '__main__':
    main()
