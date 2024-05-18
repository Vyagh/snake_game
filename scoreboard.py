from turtle import Turtle


# class Score(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.hideturtle()
#         self.speed("fastest")
#         self.penup()
#         self.goto(0, 280)
#         self.write(arg="Score: 0", align="center", font=('Arial', 13, 'normal'))
#
#     def refresh(self, user_score):
#         self.clear()
#         self.write(arg=f"Score: {user_score}", align="center", font=('Arial', 13, 'normal'))


#                                                Angela's
# She made score an attribute of scoreboard instead
# Whenever you see repeated lines of code make some sort of function or loop
# And it's always good to convert hard coded pieces of text to CONSTANTS, so it is easy to edit and change functionality

ALIGNMENT = "center"
FONT = ('courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Made this to not write this line again and again.
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
