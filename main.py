import turtle
import pandas
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
screen.tracer(0)
scoreboard = Scoreboard()


while scoreboard.score < 51:
    screen.update()
    answer = screen.textinput(title="Guess the state", prompt="What's another state's")
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    if answer in all_states:
      x = data[data["state"] == answer.capitalize()]
      trace = turtle.Turtle()
      trace.hideturtle()
      trace.penup()
      trace.goto(int(x.x), int(x.y))
      trace.write(answer)
      scoreboard.increase_score()
    else:
      pass



screen.exitonclick()