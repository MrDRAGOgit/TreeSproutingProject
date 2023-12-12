import turtle
turtle.tracer(0)
turtle.penup()
turtle.setposition(0, -200)
turtle.left(90)
turtle.pendown()
turtle.hideturtle()
import random

axiom = '2222220'
axTemp = ''
itr = 9
dl = 5
angl = 20
dangl = int(angl/2)
width = 10
turtle.pensize(width)

translate = {
    '1': '1222',
    '0': '1[-0]+0' if random.uniform(0, 1) > 0.1 else '0'
}
stc = []
for i in range(itr):
    for ch in axiom:
        if ch in translate:
            axTemp += translate[ch]
        else:
            axTemp += ch
    axiom = axTemp
    axTemp = ''
for ch in axiom:
    if ch == '0':
        turtle.pencolor(random.uniform(0, 0.5), random.uniform(0.6, 1), random.uniform(0, 0.5))
        turtle.pensize(7)
        turtle.forward(dl)
    elif ch == '1':
        turtle.pencolor(random.uniform(0.28, 0.33), random.uniform(0.12, 0.17), random.uniform(0.02, 0.07))
        turtle.forward(dl)
    elif ch == '-':
        turtle.left(angl + random.randint(-dangl, dangl))
        width *= 0.75
        turtle.pensize(width)
    elif ch == '+':
        turtle.right(angl + random.randint(-dangl, dangl))
        width *= 0.75
        turtle.pensize(width)
    elif ch == '[':
        stc.append(turtle.heading())
        stc.append(turtle.xcor())
        stc.append(turtle.ycor())
        stc.append(width)
    elif ch == ']':
        turtle.penup()
        width = stc.pop()
        turtle.sety(stc.pop())
        turtle.setx(stc.pop())
        turtle.setheading(stc.pop())
        turtle.pendown()
    elif ch == '2':
        turtle.pencolor(random.uniform(0.28, 0.33), random.uniform(0.12, 0.17), random.uniform(0.02, 0.07))
        if random.uniform(0, 1) > 0.6:
            turtle.forward(dl)
turtle.update()
turtle.mainloop()
print(axiom)