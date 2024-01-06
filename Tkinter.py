import tkinter as tk

root = tk.Tk()

root.title("CBG BANK")
root.geometry("800x500")
label = tk.Label(root, text="We Stand You", font=('Courier New', 15))
label.pack(padx = 22, pady= 22)
textbox = tk.Text(root, height=2,font=('Arial',15))
textbox.pack()
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
btn1 = tk.Button(buttonframe, text="1", font="courier")
btn1.grid(row=0, column =0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text="2", font="courier")
btn2.grid(row=0, column =1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text="3", font="courier")
btn3.grid(row=0, column =2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text="4", font="courier")
btn4.grid(row=1, column =0, sticky=tk.W + tk.E)
btn5 = tk.Button(buttonframe, text="5", font="courier")
btn5.grid(row=1, column =1, sticky=tk.W + tk.E)
btn6 = tk.Button(buttonframe, text="6", font="courier")
btn6.grid(row=1, column =2, sticky=tk.W + tk.E)
buttonframe.pack(fill='x')
root.mainloop()
