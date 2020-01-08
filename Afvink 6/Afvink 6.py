import time
import tkinter


def aftellen():
    """"Telt af met een while loop"""
    cijfer = int(input("Vanaf waar moeten we aftellen? : "))
    tijd = time.time()
    while cijfer > 0:
        print(cijfer)
        cijfer = cijfer - 1
    tijd2 = time.time()
    print("Klaar, we zijn", tijd2 - tijd, "bezig geweest.")


def recursief_aftellen(cijfer):
    """"Telt af met een recursieve loop, kan niet hoger dan 1000."""
    tijd = time.time()
    if cijfer <= 0:
        tijd2 = time.time()
        print("Klaar, we zijn", tijd2 - tijd, "bezig geweest.")
    else:
        print(cijfer)
        recursief_aftellen(cijfer - 1)


def main():
    aftellen()
    cijfer = int(input("Vanaf waar moeten we aftellen? : "))
    recursief_aftellen(cijfer)


# main()


def recursief_vermenigvuldigen(x, y, z):
    """"Vermenigvuldigt recursief de getallen die met input gedefinieerd zijn in de main"""
    if x <= 0:
        print("Het eindgetal is", z)
    else:
        z += y
        print(z, "+", y, "=", z)
        x = x - 1
        recursief_vermenigvuldigen(x, y, z)


def main2():
    x = int(input("Twee getallen vermenigvuldigen. Vul het eerste getal in: "))
    y = int(input("Twee getallen vermenigvuldigen. Vul het tweede getal in: "))
    z = 0
    recursief_vermenigvuldigen(x, y, z)


# main2()


class gui():
    """"Maakt een ster met mijn naam :x"""
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("De ster")
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame.pack(side="bottom")
        self.uitknop = tkinter.Button(self.bottom_frame, text="Sluiten", command=self.main_window.destroy)
        self.uitknop.pack()
        self.ster = tkinter.Canvas(self.main_window, width=250, height=250)
        self.ster.create_line(125,10,150,100,240,100,175,150,200,240,125,175,50,240,75,150,10,100,100,100,125,10)
        self.ster.pack()
        self.ster.create_text(125,135, text = "Dominic :D")
        tkinter.mainloop()


def main3():
    yahoo = gui()


main3()
