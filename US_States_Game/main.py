import turtle
import pandas

screen = turtle.Screen()
game_pointer = turtle.Turtle()

game_pointer.penup()
game_pointer.hideturtle()

screen.title("US States Game")

img_file = "blank_states_img.gif"
screen.addshape(img_file)
turtle.shape(img_file)

states_data = pandas.read_csv("50_states.csv")

us_state_names = states_data["state"].to_list()

score_count = 0

guessed_states = []

title_prompt = "Guess the state"

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{title_prompt}",prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missed_states = [new_item for new_item in us_state_names if new_item not in guessed_states]
        missed_states_data = pandas.DataFrame(missed_states)
        missed_states_data.to_csv("missed_states.csv")
        break

    if answer_state in us_state_names:
        score_count+=1
        guessed_states.append(answer_state)
        title_prompt=f"{score_count}/50 States Correct"
        state_info = states_data[states_data.state == answer_state]

        x_coor = int(state_info.x.item())
        y_coor = int(state_info.y.item())

        game_pointer.goto(x=x_coor,y=y_coor)
        screen._write(pos=(x_coor,y_coor),txt=f"{answer_state}",align="center",font=("Arial",10,"normal"),pencolor="black")

