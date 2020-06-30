#python program to display progress

import time
import datetime as dt
import tkinter as tk
from tkinter import messagebox
import winsound


e = Entry(master)
e.pack()
e.delete(0, END)
e.insert(0, "a default value")

print()