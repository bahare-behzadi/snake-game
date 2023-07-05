from turtle import Turtle
Font = ('Arial', 20, 'bold')
Align = "center"
class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"score= {self.score}", align=Align, font=Font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"score= {self.score}", align=Align, font=Font)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(arg="GAME OVER",move=True,  align=Align, font=Font)