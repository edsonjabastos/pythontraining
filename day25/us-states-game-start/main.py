import turtle
import os
import pandas

os.chdir(os.path.dirname(os.path.abspath(__file__)))
states_data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_names = states_data.state.tolist()
correct_states = []
no_more_states = len(correct_states) == len(states_names)
simba = turtle.Turtle()
simba.hideturtle()
simba.penup()
while not no_more_states:
    answer_state = screen.textinput(
        title=f"{len(correct_states)}/{len(states_names)} States Correct",
        prompt="What's another state's name?",
    ).title()
    if answer_state == "Exit":
        must_learn_state = states_data[~states_data.state.isin(correct_states)]
        print(must_learn_state)
        break

    if answer_state in states_names and answer_state not in correct_states:
        simba.goto(
            states_data[states_data.state == answer_state].x.item(),
            states_data[states_data.state == answer_state].y.item(),
        )
        simba.write(answer_state)
        correct_states.append(answer_state)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
must_learn_state.to_csv("vai_estudar.csv")
# turtle.mainloop()
# screen.exitonclick()
