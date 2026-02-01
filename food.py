from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        x_location = random.randint(-280, 280)
        y_location = random.randint(-280, 280)

        self.goto(x_location, y_location)

    def new_location(self):
        x_location = random.randint(-280, 280)
        y_location = random.randint(-280, 280)

        self.goto(x_location, y_location)




