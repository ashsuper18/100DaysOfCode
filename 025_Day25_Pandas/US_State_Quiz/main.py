import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = r"US_State_Quiz\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# checking the ans is in 50 state or not
data = pd.read_csv("US_State_Quiz/all_states.csv")
all_states_list = data["state"].to_list()
# getting corrdinate

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name").strip().capitalize()
    corr = data[data.state == answer_state]

    if answer_state == "Exit":
        # missing_states = []
        # final_list = [missing_states.append(state) for state in all_states_list if state not in guessed_state]
        missing_states = [
            state for state in all_states_list if state not in guessed_state]
        # CONCEPT: by loop compreshension we done 3 line of work in 1 line
        # for state in all_states_list:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        rem_states = pd.DataFrame(missing_states)
        rem_states.to_csv("You_lefts.csv")
        break

    if answer_state in all_states_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(corr.x), int(corr.y))
        t.write(answer_state)


# NOTES: to get coordinate on mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()
