#
# import os
#
#
# #Main screen
#
# master =Tk()
# master.title('Banking App')
#
# #Label
# Label(master, text="Bank App Beta", font=('calibre', 15)).pack(row=0, sticky=N, pady=10)
# Label(master, text="Your Security is Prioritized", font=('calibre', 15)).pack(row=1, sticky=N)
#
import tkinter as tk


# def Hello():
#     button = tk.Button(text="Click To Say Hi", width=15, height=2, font=('calibre', 15), bg='pink')
#     button.pack(padx=10,pady = 10 )


def convert():
    c: int = int(e1.get())
    f = c * (float(11.2))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END, f)
    t1.config(state='disabled')


window = tk.Tk()
window.title('BANKING APP BETA')
window.geometry("700x600+150+15")
name = tk.Label(window, text='Name', font=('Times', 16)).place(x=10, y=450)
email = tk.Label(window, text='Email', font=('Times', 16)).place(x=10, y=480)
password = tk.Label(window, text='password', font=('Times', 16)).place(x=10, y=505)
entry = tk.Entry(window, width=90).place(x=100, y=450)
entry = tk.Entry(window, width=90).place(x=100, y=480)
entry = tk.Entry(window, width=90).place(x=100, y=510)
#
# frame = tk.Frame()
# label_a = tk.Label(master=frame,font=('Times',16), text='This is frame A', bg='grey')
# label_a.pack()
# frame_b =tk.Frame()
# label_b =tk.Label(master=frame_b, font=('Times',16),text='This is frame B', bg='blue')
# label_b.pack()
# frame.pack()
# frame_b.pack()
colour_frame_1 = tk.Frame(window, width=90, height=20, bg='red')
colour_frame_1.pack(fill=tk.X)
colour_frame_2 = tk.Frame(window, width=90, height=10, bg='yellow')
colour_frame_2.pack(fill=tk.X)
colour_frame_3 = tk.Frame(window, width=90, height=10, bg='green')
colour_frame_3.pack(fill=tk.X)

l1 = tk.Label(window, text='Amount in USD', font=('Times', 16), bg='purple')

l2 = tk.Label(window, text='GHS equivalent', font=('Times', 16), bg='purple')

e1 = tk.Entry(window, font=('Times', 17))

t1 = tk.Text(window, font=('Times', 16), width=30, height=2)

button = tk.Button(window, text='Converter', font=('Times', 14))

l1.pack()
l2.pack()
e1.pack()
button.pack()
t1.pack()
convert()
window.mainloop()
