import tkinter
class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack(side = "top")
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame.pack(side = "bottom")
        self.label1 = tkinter.Label(self.bottom_frame, text="Za Warudo", bg = "purple")
        self.label1.pack(side = "left")
        self.label2 = tkinter.Label(self.bottom_frame, text = "is kerstvakantie", bg = "green")
        self.label2.pack(side = "left")
        self.label3 = tkinter.Label(self.top_frame, text = "ok boomer", bg = "gray")
        self.label3.pack(side = "right")
        self.main_window.mainloop()
my_gui = GUI()
