from tkinter import *
class Display():
    def __init__(self):
        self.display = Tk()
        self.display.geometry("800x480")
        self.display.config(bg='#404040')
        self.createWidgets()

    def updateTask(self):
        while True:
            global text
            text = input()
            self.lblSpeed.configure(text=text)

    def quit(self):
        self.display.quit()

    def printHello(self):
        print("Hello")

    def createWidgets(self):
        self.display.btn = (self,
                     text="X",
                     fg='black',
                     command=quit)
        self.display.btn.place(x=780, y=5)

        lblClose = self.display.Label(self,
                         text="Close",
                         fg='white',
                         bg='#404040',
                         font=("Helvetica", 11))
        lblClose.place(x=735, y=5)

        lblSpeed = Label(self,
                         text="0",
                         bg='#404040',
                         fg="white",
                         font=("Helvetica", 30))
        lblSpeed.place(relx=.5, rely=.5, anchor=CENTER)

        lblKMH = Label(display,
                       text='Km/h',
                       bg='#404040',
                       fg='white',
                       font=("Helvetica", 20))
        lblKMH.place(relx=.5, rely=.55, anchor=N)

        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)  # exits background (gui) thread
        self.quitButton.grid(row=1, column=0)
        self.printButton = tk.Button(self, text='Print', command=lambda: self.printHello())
        self.printButton.grid(row=1, column=1)