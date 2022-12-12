import turtle

kura = turtle.Turtle()
ruka = turtle.Screen()

ruka.bgcolor('black')
kura.pencolor('lime')
kura.speed(100)

warna = ('aqua', 'blue', 'green', 'lime', 'red', 'orange', 'yellow', 'purple')

for banyakLayer in range(9):
    for banyakKelopak in range(12):
        kura.speed(banyakKelopak+10)
        for i in range(2):
            kura.pensize(2)
            kura.circle(80+banyakLayer*16, 90)
            kura.lt(90)
        kura.lt(30)
    kura.pencolor(warna[banyakLayer%8])
ruka.exitonclick()