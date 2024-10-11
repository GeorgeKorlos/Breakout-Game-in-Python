from turtle import Turtle

class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color("green")
        self.penup()
        self.goto(x, y)

    def destroy(self):
        self.goto(1000, 1000)  
