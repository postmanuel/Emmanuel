import tkinter as tk
from tkinter import messagebox


class MyGUI:
    def __int__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Message", font=('Arial', 15))
        self.label.pack()
        self.textbox = tk.Text(self.root, height=4, font=('Arial', 15))
        self.textbox.bind("<KeyPres>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Message", font=('Arial', 15),
                                    variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 15),
                                command=self.show_message)
        self.button.pack(padx=10, pady=10)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="message", message=self.textbox.get('1.0', tk.END))

    def shortcut (self, event):
        print(event)


MyGUI()