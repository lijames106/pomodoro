
import time
import datetime as dt

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import winsound
# hide main window
root = tkinter.Tk()
root.withdraw()



## Main script here:
# Collect time information
t_now = dt.datetime.now()                       # Current time for reference.   [datetime object]
t_pom = 25*60                                   # Pomodoro time                 [int, seconds]
t_delta = dt.timedelta(0,t_pom)                 # Time delta in mins            [datetime object]
t_fut = t_now + t_delta                         # Future time for reference     [datetime object]
delta_sec = 1#60                                  # Break time, after pomodoro    [int, seconds]
t_fin = t_now + dt.timedelta(0,t_pom+delta_sec) # Final time (w/ 5 mins break)  [datetime object]

# GUI set pomodoro in motion!
messagebox.showinfo("Pomodoro Started!", "\nIt is now "+t_now.strftime("%H:%M") +
" hrs. \nTimer set for 25 mins.")