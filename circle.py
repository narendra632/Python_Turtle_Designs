# Draw spiral circles
import turtle as t
t.Screen().bgcolor("black")
t.pensize(2)
t.speed(11)

for i in range(100):
    for color in ("red", "magenta", "blue", "cyan", "green", "white", "yellow"):
        t.color(color)
        t.circle(150)
        t.left(16) 
    t.hideturtle()
t.done()
