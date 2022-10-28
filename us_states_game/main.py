import turtle
import pandas as pd
import time


screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
score = 0
states_df = pd.read_csv('50_states.csv')
all_states = states_df.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Guessed',
                                    prompt="What's another state's name?")
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv', index=False)
        break
    if answer_state.title() in all_states:
        guessed_states.append(answer_state)
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        answer = states_df[states_df.state == answer_state.title()]
        answer_turtle.goto(int(answer.x), int(answer.y))
        answer_turtle.write(answer_state.title())
        time.sleep(.5)
