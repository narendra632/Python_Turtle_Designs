# draw rainbow benzene
import turtle as t
colors = ["red", "purple", "green", "orange", "blue","pink"]
t.Pen()
t.speed(11)

t.bgcolor("black")
for x in range(1000):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
t.done()
    #try 50, 60, 80, 90, 100, 200, 250, 300, 500, 600, 800