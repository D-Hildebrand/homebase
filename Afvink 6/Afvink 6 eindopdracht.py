# Door Dominic Hildebrand, eindelijk af op 5-1-2020
import random
import tkinter


class slakkenrace():
    """Maakt een race met"""

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Slakkenrace")
        self.race = tkinter.Canvas(self.main_window, width=500, height=500)
        self.uitknop = tkinter.Button(self.main_window, text="Sluiten", command=self.main_window.destroy)
        self.uitknop.pack(side="bottom")
        self.race.create_line(400, 0, 400, 500, width=10, fill='cyan')
        self.sara = 1
        self.jason = 1
        self.michael = 1
        self.rose = 1
        while self.sara and self.jason and self.michael and self.rose < 420:
            self.race.create_line(0, 100, self.sara, 100, width=50, fill='yellow')
            self.race.create_line(0, 200, self.jason, 200, width=50, fill='brown')
            self.race.create_line(0, 300, self.michael, 300, width=50, fill='blue')
            self.race.create_line(0, 400, self.rose, 400, width=50, fill='red')
            self.sara += random.randint(1, 6)
            self.jason += random.randint(1, 6)
            self.michael += random.randint(1, 6)
            self.rose += random.randint(1, 6)
            self.race.update()  # Hiermee gaat het stuk voor stuk vooruit
            self.race.pack()
        tkinter.mainloop()


boop = slakkenrace()
