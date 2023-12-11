import turtle
turtle.tracer(0)
turtle.penup()
turtle.setposition(-380, 300)
turtle.pendown()
turtle.pensize(2)
turtle.hideturtle()

axiom = 'F+F+F+F'
axTemp = ''
itr = 3

translate = {
    '+': '+',
    '-': '-',
    'F': 'F+F-F-F+F'
}
for i in range(itr):
    for ch in axiom:
        axTemp += translate[ch]
    axiom = axTemp
    axTemp = ''
for ch in axiom:
    if ch == '+':
        turtle.right(90)
    elif ch == '-':
        turtle.left(90)
    else:
        turtle.forward(15)
turtle.update()
turtle.mainloop()
turtle.clear()
