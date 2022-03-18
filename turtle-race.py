from turtle import Turtle, Screen
import random
import ctypes

# Screen setup
screen = Screen()
screen.setup(width=500, height= 400)

# Initial variables
offset = -100
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtles_list = []

# Generating turtle objects and putting them in a array
for color in colors:
    t = Turtle(shape="turtle")
    t.pu()
    t.color(color)
    t.goto(x = -230, y = offset)
    offset += 40
    turtles_list.append(t)

# If this is one, the race is going on
if user_bet:
    is_race_on = True

# Main game logic
while is_race_on:

    # Taking each turtle from the list
    for turtle in turtles_list:

        # Moving a turtle
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

        # If any turtle reached the finish, display a message, stop the race
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                #print(f"You've won! The {winning_color} turtle is the winner!")
                ctypes.windll.user32.MessageBoxW(0, f"You've won! The {winning_color} turtle is the winner!", "You've won", 1)
            else:
                ctypes.windll.user32.MessageBoxW(0, f"You've lost! The {winning_color} turtle is the winner!", "You've lost", 1)

screen.exitonclick()