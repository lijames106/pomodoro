#python program to display timer and have button to start
#25 min timer, can write what the timer is for

import time
import datetime as dt
import tkinter
from tkinter import messagebox
import winsound

current = dt.datetime.now()
change = dt.timedelta(0, 1500)
future = current + changefinish = now + dt.timedelta(0,1800)

root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("Pomodoro", "\nIt is " + current.strftime("%H:%M") + " hrs.\nTimer set for 25 minutes.")
  
while True:
    #loop until time passes
    if current < future:
        print()
    elif future <= current <= :
        print()
    else:
        print()
    print()
    time.sleep()
    timewnow = 