from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(10)


def move_back():
    t.back(10)


def clockwise():
    t.right(10)


def c_clockwise():
    t.left(10)


def clear():
    t.reset()


s.listen()
s.onkey(move_forward, "w")
s.onkey(move_back, "s")
s.onkey(clockwise, "d")
s.onkey(c_clockwise, "a")
s.onkey(clear, "c")
s.exitonclick()
