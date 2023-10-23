from turtle import Turtle
import time

FONT = ("Courier", 12, "normal")


class Difficulty(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.write("Choose difficulty by pressing a button:\n1. easy\n2. medium\n3. hard\n4. manic", font=FONT,
                   align="center")
        self.difficulty = []
        self.difficulty_set = False

    def easy_difficulty(self):
        self.difficulty = [1]
        self.set_difficulty()

    def medium_difficulty(self):
        self.difficulty = [1, 2]
        self.set_difficulty()

    def hard_difficulty(self):
        self.difficulty = [1, 2, 3]
        self.set_difficulty()

    def manic_difficulty(self):
        self.difficulty = [1, 2, 3, 4]
        self.set_difficulty()

    def set_difficulty(self):
        self.difficulty_set = True
        self.clear()

    def empty_method(self):
        pass
