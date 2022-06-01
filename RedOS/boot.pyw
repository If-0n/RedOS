from cgi import test
from cgitb import text
from ensurepip import bootstrap
from importlib.metadata import files
from logging import shutdown
from random import shuffle
from re import X
from struct import pack
import tkinter as tk
from tkinter import OFF, Y, Canvas, Label
from tkinter.messagebox import NO
from turtle import bgcolor, color, title
import subprocess
import os


#Window setup
root = tk.Tk()
root.title("RedOS Boot")
root.geometry("500x500")
root.resizable(False, False)




#Actual window
window = tk.Canvas(root, height=501, width=501,bg="#000000", highlightthickness=0)
window.pack()

#title
title = tk.Label(root, height=2, width=14, bg="#000000", fg="#999999",text="RedOS", font=("Helvetica", 25),)
title.pack()
title.place(x=125, y=5)
#files
def OnClickBoot():
    subprocess.Popen("C:\Program Files (x86)\Klox\RedOS\RedOS.bat")


boot = tk.Button(root, height=1, width=9, bg="#999999", text="Boot", relief="sunken", font=("Helvetica", 25), command=OnClickBoot )
boot.pack()
boot.place(x=175, y=125)

#commands





root.mainloop()