from tkinter import *
import time
import threading
from src.display import Display
#from src.Tacho import Tacho

#Tacho.updateTacho(50)

global text
def updateTask():
    while True:
        global text
        text = input()
        lblSpeed.configure(text=text)
        time.sleep(0.5)

def quit():
    display.quit()

display = Tk()
display.geometry("800x480")
display.config(bg='#404040')

btn = Button(display,
             text="X",
             fg='black',
             command=quit)
btn.place(x=780, y=5)

lblClose = Label(display,
                 text="Close",
                 fg='white',
                 bg='#404040',
                 font=("Helvetica", 11))
lblClose.place(x=735, y=5)

lblSpeed = Label(display,
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

Background = threading.Thread(target=updateTask)
Background.start()

display.title('GUI')
display.mainloop()

def runtinker():
    app = Display()
