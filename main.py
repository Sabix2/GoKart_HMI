import time
import tkinter as tk
from src.Display import Display

if __name__ == "__main__":
    root = tk.Tk()
    # removes the windows title bar CHECK ON LINUX!!!
    #root.overrideredirect(True)
    root.resizable(0,0)
    app = Display(root)
    root.mainloop()
