#python program to display timer and have button to start
#25 min timer + 5 min break, can write what the timer is for and adjust time length

import time
import datetime as dt
import tkinter as tk
from tkinter import messagebox
import winsound

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Pomodoro", "\nIt is " + current.strftime("%H:%M") + ".\nTimer set for 25 minutes.")

#please print a number
e = Entry()

now = dt.datetime.now()
delta = dt.timedelta(0, 1500)
breaktime = now + delta
end = now + dt.timedelta(0, total)

while True:
    #loop until time passes
    if now < breaktime:#during pomodoro
        print()
    elif breaktime <= now < end: #during break
        print()
    else:  #end
        print()
    print()
    time.sleep()
    timewnow = 