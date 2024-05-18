from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")    # can use .shape because we inherited it
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)    # we halved it from 20x20 to 10x10
        self.color("CornflowerBlue")

        # So we do not see it being created and moving somewhere animation
        self.speed("fastest")

        self.refresh()

    def refresh(self):  # To Refresh the food location on contact
        # Subtract the screen edges
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


#                                                Project Flow
# We will not do self.food = Turtle() this (making a food object which is actually from a Turtle class)
# But we need this class Food to inherit from Turtle class
# Once adding Food(Turtle) the init line of Food gives us error that call to super class init is missing
