import tkinter as tk
from tkinter import ttk
import ctypes
import time
import keyboard

mouse = ctypes.windll.user32
state = False

def StateFalse():
    global state
    global x
    if state == True:
        state = False
        x = 0

def StateTrue():
    global state
    if state == True:
        state = False
    else:
        state = True

def autoclick():
    global state
    global x
    global timekeeper

    timekeeper += 1
    if state == True:
        Amount = int(amount.get())
        Speed = int(speed.get())
        if Amount == 0:
            time.sleep(Speed / 1000)
            mouse.mouse_event(2, 0, 0, 0, 0)  # left mouse button down
            mouse.mouse_event(4, 0, 0, 0, 0)  # left mouse button up
            x += 1
            print("Clicked %s Times" % (x))
        elif x < Amount and state == True:
            time.sleep(Speed / 1000)
            mouse.mouse_event(2, 0, 0, 0, 0)  # left mouse button down
            mouse.mouse_event(4, 0, 0, 0, 0)  # left mouse button up
            x += 1
            print("Clicked %s Times" % (x))
            if x == Amount:
                state = False
    root.after(10, autoclick)

def toggle_autoclick(event):
    StateTrue() if not state else StateFalse()

root = tk.Tk()
root.title("AutoClicker")
root.resizable(width=False, height=False)

amount = tk.StringVar()
speed = tk.StringVar()

amount.set(str(0))
speed.set(str(100))

mainframe = ttk.Frame(root)
mainframe.grid(padx=5, pady=5)

amountLabel = ttk.Label(mainframe, text="Number of Clicks\n(set to 0 for infinite)")
amountLabel.grid(column=1, row=1, sticky=tk.W)

speedLabel = ttk.Label(mainframe, text="Click interval\n(In milliseconds)")
speedLabel.grid(column=1, row=2, sticky=tk.W)

amountEntry = ttk.Entry(mainframe, textvariable=amount, width=5)
amountEntry.grid(column=2, row=1)

speedEntry = ttk.Entry(mainframe, textvariable=speed, width=5)
speedEntry.grid(column=2, row=2)

startButton = ttk.Button(mainframe, text="Start", width=10, command=StateTrue)
startButton.grid(column=1, row=3, columnspan=2, sticky=tk.W)

stopButton = ttk.Button(mainframe, text="Stop", width=10, command=StateFalse)
stopButton.grid(column=2, row=3, columnspan=2, sticky=tk.E)

x = 0
timekeeper = 0

keyboard.on_press_key("F6", toggle_autoclick)
root.after(10, autoclick)
root.mainloop()
