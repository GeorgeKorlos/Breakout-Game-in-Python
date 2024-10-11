import turtle
from paddle import Paddle
from ball import Ball
from brick import Brick

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0) 

paddle = Paddle()
ball = Ball()

bricks = []
brick_rows = 5
brick_cols = 10
x_start = -350
y_start = 250
for row in range(brick_rows):
    for col in range(brick_cols):
        x = x_start + col * 80
        y = y_start - row * 40
        bricks.append(Brick(x, y))

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

running = True
lives = 3
score = 0

while running:
    screen.update()
    ball.move()

    if ball.ycor() < -240 and ball.distance(paddle) < 50:
        ball.bounce_y()

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()
    if ball.ycor() > 290:
        ball.bounce_y()
    if ball.ycor() < -290:
        lives -= 1
        ball.reset_position()
        if lives == 0:
            running = False
            print("Game Over")

    for brick in bricks:
        if ball.distance(brick) < 35 and brick.isvisible():
            ball.bounce_y()
            brick.destroy()
            score += 1

    if all(not brick.isvisible() for brick in bricks):
        running = False
        print("You Win!")

screen.exitonclick()
