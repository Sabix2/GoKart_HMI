import time
import tkinter as tk
from tkinter import ttk


class Display:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x480')

        self.root.title('GoKart HMI')
        self.frame = tk.Frame(self.root, background='#404040')
        self.frame.pack(fill='both', expand=True)

        self.time_label = tk.Label(self.frame, text='0', bg='#404040', fg='white')
        self.time_label.pack()

        self.quit_button = tk.Button(self.frame, text="x", command=self.quit)
        self.quit_button.place(x=780, y=5)

        self.quit_label = tk.Label(self.frame, text='Close', fg='white', bg='#404040', font=("Helvetica", 11))
        self.quit_label.place(x=735, y=5)

        self.speed_label = tk.Label(self.frame, text="speed", bg='#404040', fg="white", font=("Terminal", 30))
        self.speed_label.place(x=400, y=240, anchor='center')

        self.kmh_label = tk.Label(self.frame, text='km/h', bg='#404040', fg='white', font=("Helvetica", 18))
        self.kmh_label.place(x=400, y=255, anchor='n')

        self.kmh_textbox = tk.Text(self.frame, height=1, width=15)
        self.kmh_textbox.place(x=400, y=400)

        self.battery_pb = ttk.Progressbar(orient=tk.VERTICAL, maximum=100)
        self.battery_pb.place(x=50, y=200, height=200)
        self.percent = 0

        self.background()

    def background(self):
        self.time_label['text'] = time.asctime()
        self.speed_label.config(text=self.kmh_textbox.get("1.0", "end-1c"))
        self.percent = self.updateBattery(self.percent)
        self.root.after(1, self.background)

    def quit(self):
        self.root.quit()

    def updateBattery(self, percentage: int):
        percentage = 0.1
        if percentage >= 100:
            percentage = 0
        print(percentage)
        self.battery_pb.step(percentage)
        return percentage
