import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. State Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=700, height=550)

# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinate)
states_data = pandas.read_csv("50_states.csv")
states_name = states_data["state"]
states_list = states_name.to_list()
# print(states_list)
correct_answered_list = []
while not len(correct_answered_list) == 50:
    user_enter_state = screen.textinput(title=f"{len(correct_answered_list)}/50 states correct", prompt="Enter any U.S."
                                                                                                        "state:").title()
    if user_enter_state == "Exit":
        break

    if user_enter_state in states_list:
        correct_answered_list.append(user_enter_state)
        x_coordinate = int(states_data[states_name == user_enter_state]['x'])
        y_coordinate = int(states_data[states_name == user_enter_state]['y'])
        turtle_1 = turtle.Turtle()
        turtle_1.penup()
        turtle_1.hideturtle()
        turtle_1.setposition(x=x_coordinate, y=y_coordinate)
        turtle_1.write(user_enter_state, font=("Arial", 6, 'bold'))

# turtle.mainloop()
for answered_states in correct_answered_list:
    states_list.remove(answered_states)

series = pandas.Series(states_list)
series.to_csv("states_to_learn.csv")

