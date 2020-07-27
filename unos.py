import turtle
strelica = turtle.getturtle()


def unos(unos, x, y):
    strelica.penup()
    strelica.setposition(x, y)
    strelica.write(unos, font=("Arial", 16, "normal"))
