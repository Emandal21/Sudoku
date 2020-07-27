import turtle
from unos import *
import random


strelica = turtle.getturtle()
turtle.setup(800, 600)
prozor = turtle.Screen()
prozor.title("SUDOKU")
strelica.speed(0)


def kvadrat(a):    # a je duzina stranice
    strelica.pendown()
    strelica.forward(a)
    strelica.left(90)
    strelica.forward(a)
    strelica.left(90)
    strelica.forward(a)
    strelica.left(90)
    strelica.forward(a)
    strelica.left(90)


def kucica(x, y):
    strelica.penup()
    strelica.setposition(x, y)
    strelica.pendown()
    kvadrat(40)
    strelica.setposition(x + 40, y)
    kvadrat(40)
    strelica.setposition(x + 80, y)
    kvadrat(40)
    strelica.penup()
    strelica.setposition(x, y + 40)
    strelica.pendown()
    kvadrat(40)
    strelica.setposition(x + 40, y + 40)
    kvadrat(40)
    strelica.setposition(x + 80, y + 40)
    kvadrat(40)
    strelica.penup()
    strelica.setposition(x, y + 80)
    strelica.pendown()
    kvadrat(40)
    strelica.setposition(x + 40, y + 80)
    kvadrat(40)
    strelica.setposition(x + 80, y + 80)
    kvadrat(40)
    strelica.pensize(3)
    strelica.penup()
    strelica.setposition(x, y)
    strelica.pendown()
    kvadrat(120)
    strelica.pensize(0)


def provjeraKucica(broj, kolona, red):
    if kolona == "A" or kolona == "a" or kolona == "B" or kolona == "b" or kolona == "C" or kolona == "c":
        if red in [1, 2, 3]:
            if broj in kucica1:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)
        elif red in [4, 5, 6]:
            if broj in kucica4:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)
        elif red in [7, 8, 9]:
            if broj in kucica7:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)
    if kolona == "D" or kolona == "d" or kolona == "E" or kolona == "e" or kolona == "F" or kolona == "f":
        if red in [1, 2, 3]:
            if broj in kucica2:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)
        elif red in [4, 5, 6]:
            if broj in kucica5:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)
        elif red in [7, 8, 9]:
            if broj in kucica8:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)
    if kolona == "G" or kolona == "g" or kolona == "H" or kolona == "h" or kolona == "I" or kolona == "i":
        if red in [1, 2, 3]:
            if broj in kucica3:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)
        elif red in [4, 5, 6]:
            if broj in kucica6:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)
        elif red in [7, 8, 9]:
            if broj in kucica9:
                print("Greska: Broj vec postoji u datoj kucici!")
                return(False)
            else:
                return(True)


def provjeraRed(broj, red):
    if red == 1:
        if broj in red1:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)
    elif red == 2:
        if broj in red2:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)
    elif red == 3:
        if broj in red3:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)
    elif red == 4:
        if broj in red4:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)
    elif red == 5:
        if broj in red5:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)
    elif red == 6:
        if broj in red6:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)
    elif red == 7:
        if broj in red7:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)
    elif red == 8:
        if broj in red8:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)
    elif red == 9:
        if broj in red9:
            print("Greska: Broj vec postoji u datom redu!")
            return(False)
        else:
            return(True)


def provjeraKolona(broj, kolona):
    if (kolona == "A") or (kolona == "a"):
        if broj in A:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)
    elif (kolona == "B") or (kolona == "b"):
        if broj in B:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)
    elif (kolona == "C") or (kolona == "c"):
        if broj in C:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)
    elif (kolona == "D") or (kolona == "d"):
        if broj in D:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)
    elif (kolona == "E") or (kolona == "e"):
        if broj in E:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)
    elif (kolona == "F") or (kolona == "f"):
        if broj in F:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)
    elif (kolona == "G") or (kolona == "g"):
        if broj in G:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)
    elif (kolona == "H") or (kolona == "h"):
        if broj in H:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)
    elif (kolona == "I") or (kolona == "i"):
        if broj in I:
            print("Greska: Broj vec postoji u datoj koloni!")
            return(False)
        else:
            return(True)


kucica(-200, -200)
kucica(-80, -200)
kucica(40, -200)
kucica(-200, -80)
kucica(-80, -80)
kucica(40, -80)
kucica(-200, 40)
kucica(-80, 40)
kucica(40, 40)    # iscrtavanje kucica sudokua

unos("A", -190, 175)
unos("B", -150, 175)
unos("C", -110, 175)
unos("D", -70, 175)
unos("E", -30, 175)
unos("F", 10, 175)
unos("G", 50, 175)
unos("H", 90, 175)
unos("I", 130, 175)    # pise slova za kolone iznad table sudokua

unos("9", -215, -190)
unos("8", -215, -150)
unos("7", -215, -110)
unos("6", -215, -70)
unos("5", -215, -30)
unos("4", -215, 10)
unos("3", -215, 50)
unos("2", -215, 90)
unos("1", -215, 130)    # pise brojeve koji predstavljaju redove na lijevoj strani table sudoku


izbor = random.randint(1, 4)
if izbor == 1:
    from sudoku1 import *
if izbor == 2:
    from sudoku2 import *
if izbor == 3:
    from sudoku3 import *
if izbor == 4:
    from sudoku4 import *


while (a != 9) or (b != 9) or (c != 9) or (d != 9) or (e != 9) or (f != 9) or (g != 9) or (h != 9) or (i != 9):
    kolona = input("Unesite zeljenu kolonu od A do I: ")
    red = eval(input("Unesite zeljeni red od 1 do 9: "))
    broj = eval(input("Koji broj zelite unijeti? "))

    pk = provjeraKucica(broj, kolona, red)
    pr = provjeraRed(broj, red)
    pkl = provjeraKolona(broj, kolona)

    if pk and pr and pkl:
        if (kolona == "A") or (kolona == "a"):
            A.append(broj)
            a += 1
            x = -190
        if (kolona == "B") or (kolona == "b"):
            B.append(broj)
            b += 1
            x = -150
        if (kolona == "C") or (kolona == "c"):
            C.append(broj)
            c += 1
            x = -110
        if (kolona == "D") or (kolona == "d"):
            D.append(broj)
            d += 1
            x = -70
        if (kolona == "E") or (kolona == "e"):
            E.append(broj)
            e += 1
            x = -30
        if (kolona == "F") or (kolona == "f"):
            F.append(broj)
            f += 1
            x = 10
        if (kolona == "G") or (kolona == "g"):
            G.append(broj)
            g += 1
            x = 50
        if (kolona == "H") or (kolona == "h"):
            H.append(broj)
            h += 1
            x = 90
        if (kolona == "I") or (kolona == "i"):
            I.append(broj)
            i += 1
            x = 130

        if red == 1:
            red1.append(broj)
            y = 130
        if red == 2:
            red2.append(broj)
            y = 90
        if red == 3:
            red3.append(broj)
            y = 50
        if red == 4:
            red4.append(broj)
            y = 10
        if red == 5:
            red5.append(broj)
            y = -30
        if red == 6:
            red6.append(broj)
            y = -70
        if red == 7:
            red7.append(broj)
            y = -110
        if red == 8:
            red8.append(broj)
            y = -150
        if red == 9:
            red9.append(broj)
            y = -190

        if kolona == "A" or kolona == "a" or kolona == "B" or kolona == "b" or kolona == "C" or kolona == "c":
            if red in [1, 2, 3]:
                kucica1.append(broj)
            elif red in [4, 5, 6]:
                kucica4.append(broj)
            elif red in [7, 8, 9]:
                kucica7.append(broj)
        if kolona == "D" or kolona == "d" or kolona == "E" or kolona == "e" or kolona == "F" or kolona == "f":
            if red in [1, 2, 3]:
                kucica2.append(broj)
            elif red in [4, 5, 6]:
                kucica5.append(broj)
            elif red in [7, 8, 9]:
                kucica8.append(broj)
        if kolona == "G" or kolona == "g" or kolona == "H" or kolona == "h" or kolona == "I" or kolona == "i":
            if red in [1, 2, 3]:
                kucica3.append(broj)
            elif red in [4, 5, 6]:
                kucica6.append(broj)
            elif red in [7, 8, 9]:
                kucica9.append(broj)

        strelica.pencolor("blue")
        unos(broj, x, y)

strelica.pencolor("red")
strelica.setposition(-200, 200)
strelica.write("KRAJ IGRE!", font=("Arial", 32, "bold"))

turtle.exitonclick()

