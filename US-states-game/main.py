import turtle
import pandas

ALIGNMENT = 'center'
FONTNAME = ('Courier', 10, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
# screen.tracer(0)
# #Data of 50-states CSV
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
print(states_list)

correct_guesses = []

guessed = 0

game_is_on = True

while len(correct_guesses) < 50 and game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in correct_guesses]
        datas = pandas.DataFrame(missing_states)
        datas.to_csv("states_to_learn.csv")
        game_is_on = False

    if answer_state in states_list:
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        each_state = data[data.state == answer_state]
        state_x = each_state.x.tolist()
        state_y = each_state.y.tolist()
        x = state_x[0]
        y = state_y[0]
        t.goto(int(x), int(y))
        t.write(answer_state)
        guessed += 1

