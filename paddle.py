from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("blue")
        self.penup()
        self.goto(0, -250)
        self.speed(0)
        self.base_speed = 30  
        self.speed_multiplier = 2.0  

    def move_left(self):
        x = self.xcor() - self.base_speed * self.speed_multiplier
        if x > -350:
            self.goto(x, self.ycor())

    def move_right(self):
        x = self.xcor() + self.base_speed * self.speed_multiplier
        if x < 350:
            self.goto(x, self.ycor())
    
    def increase_speed(self):
        self.speed_multiplier += 0.3
