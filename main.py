from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
tim.heading()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)
    print("hellow man")


def clockwise():
    for i in range(2):
        tim.speed("fastest")
        tim.right(10)
        tim.forward(10)


def counter_clockwise():
    for i in range(2):
        tim.speed("fastest")
        tim.left(10)
        tim.forward(10)


def clear_drawing():
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()
