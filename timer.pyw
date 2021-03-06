
#python program to display timer and have button to start
#25 min timer + 5 min break, can write what the timer is for and adjust time length

import time
import datetime as dt
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import winsound

root = tkinter.Tk()
root.withdraw()


#please print a number
#e = Entry(master)
#e.pack()
#e.delete(0, END)
#e.insert(0, "a default value")

now = dt.datetime.now()
delta = dt.timedelta(0, 1500)
breaktime = now + delta
total = 30*60
#end = now + dt.timedelta(0, total)#change to total to customize

messagebox.showinfo("Pomodoro", "\nIt is " + current.strftime("%H:%M") + ".\nTimer set for 25 minutes.")

while True:
    #loop until time passes
    if now < breaktime:#during pomodoro
        print('working')
    elif breaktime <= now < end: #during break
        print("break")
    else:  #end
        print("fin")
        for i in range(5):
            winsound.Beep((i+50), 400)
        restart = messagebox.askyesno()
        if restart == True:
            now = dt.datetime.now()
            end = now + dt.timedelta(0, total)#change to total to customize
            continue
        else:
            messagebox.showinfo("pomodoro Finished!", )
            break
    print()
    time.sleep(30)
    now = dt.datetime.now()
print('\n\nITS OVER YOURE THROUGH\n\n')
