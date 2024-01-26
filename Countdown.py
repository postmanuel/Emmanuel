from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('CountDown')

def time():
    string = strftime('%H:%M:%S  %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("castellar", 85), background='black', foreground='cyan')
label.pack(anchor='center')


time()


mainloop()