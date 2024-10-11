from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(0, -230)
        self.dx = 2
        self.dy = 2

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1

    def reset_position(self):
        self.goto(0, -230)
        self.dx = max(1, self.dx * 0.9)  
        self.dy = max(1, self.dy * 0.9)  
