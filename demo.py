import os
import turtle

# Set up the first page

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgpic("background_image_1.png")

# create the turtle for drawing the buttons
button_turtle = turtle.Turtle()
button_turtle.penup()
button_turtle.hideturtle()

# create the Start button
button_turtle.goto(0, 0)
button_turtle.color("white")
button_turtle.fillcolor("gray")
button_turtle.begin_fill()
button_turtle.goto(-100,50)
button_turtle.pendown()
button_turtle.goto(100,50)
button_turtle.goto(100,-50)
button_turtle.goto(-100,-50)
button_turtle.goto(-100,50)
button_turtle.end_fill()
button_turtle.penup()
button_turtle.goto(0, -10)  # move the button up by 35 pixels
button_turtle.write("Start", align="center", font=("Arial", 20, "normal"), move=True)
button_turtle.goto(-100, 0)

# create the Quit button
button_turtle.goto(-350, -250)
button_turtle.color("white")
button_turtle.fillcolor("gray")
button_turtle.begin_fill()
button_turtle.goto(-275, -250)
button_turtle.pendown()
button_turtle.goto(-275, -200)
button_turtle.goto(-350, -200)
button_turtle.goto(-350, -250)
button_turtle.goto(-275, -250)
button_turtle.end_fill()
button_turtle.penup()
button_turtle.goto(-330, -235)  # move turtle to center of button
button_turtle.write("Quit", align="left", font=("Arial", 14, "normal"))

# function to quit the game
def quit_game(x, y):
    turtle.bye()

# function to handle the Start button click
def next_page(x, y):
    # Remove existing buttons
    button_turtle.clear()

    # Call the second_page function
    second_page()

# Set up event listener for start button
turtle.onscreenclick(next_page)

# Set up event listener for quit button
turtle.onkeypress(quit_game, "q")

# Define the second page
def second_page():
    # Create screen and background
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgpic("background_image_2.png")

    # Create turtles for drawing buttons
    button_turtle_1 = turtle.Turtle()
    button_turtle_1.hideturtle()
    button_turtle_1.penup()
    button_turtle_2 = turtle.Turtle()
    button_turtle_2.hideturtle()
    button_turtle_2.penup()

    # Create buttons
    button_turtle_1.color("white")
    button_turtle_1.fillcolor("gray")
    button_turtle_1.goto(-150, 50)
    button_turtle_1.begin_fill()
    for i in range(2):
        button_turtle_1.forward(300)
        button_turtle_1.right(90)
        button_turtle_1.forward(50)
        button_turtle_1.right(90)
    button_turtle_1.end_fill()
    button_turtle_1.goto(0, 35)
    button_turtle_1.write("Button 1", align="center", font=("Arial", 20, "normal"), move=True)
    button_turtle_2.color("white")
    button_turtle_2.fillcolor("gray")
    button_turtle_2.goto(-150, -50)
    button_turtle_2.begin_fill()
    for i in range(2):
        button_turtle_2.forward(300)
        button_turtle_2.right(90)
        button_turtle_2.forward(50)
        button_turtle_2.right(90)
    button_turtle_2.end_fill()
    button_turtle_2.goto(0, -15)
    button_turtle_2.write("Button 2", align="center", font=("Arial", 20, "normal"), move=True)

    # function to handle Button 1 click
    def button_1_click(x, y):
        button_turtle_1.clear()
        button_turtle_2.clear()
        button_turtle_1.write("Button 1 clicked", align="center", font=("Arial", 20, "normal"), move=True)

    # function to handle Button 2 click
    def button_2_click(x, y):
        button_turtle_1.clear()
        button_turtle_2.clear()
        button_turtle_2.write("Button 2 clicked", align="center", font=("Arial", 20, "normal"), move=True)

    # Set up event listeners for buttons
    button_turtle_1.onclick(button_1_click)
    button_turtle_2.onclick(button_2_click)

turtle.mainloop()