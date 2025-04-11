import turtle
t=turtle.Turtle()
s=turtle.Screen()
jump = t.penup
def jump(t, x, y):
    'faz a tartaruga pular para as coordenadas x, y'
    t.penup()
    t.goto(x, y)
    t.pendown()
def olimpiadas(t):
    'faz a tartaruga desenhar o simbolo das olimpiadas'
    t.pensize(5)
    jump(t, 0, 0)
    t.setheading(0)
    t.circle(100)
    jump(t, -220, 0)
    t.circle(100)
    jump(t, 220, 0)
    t.circle(100)
    jump(t, 110, -100)
    t.circle(100)
    jump(t, -110, -100)
    t.circle(100)
olimpiadas(t)
s.exitonclick()
turtle.mainloop()