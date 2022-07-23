import random
import tkinter as tk

root = tk.Tk()
root.title(".?.")
root.geometry('180x210')
root.resizable(False, False)


def coinflip():
    flip = random.randint(0, 1)
    if flip == 0:
        frame.picture = tk.PhotoImage(file="C:/Users/matve-il/PycharmProjects/CoinFlip/ruble_res.PNG")
        frame.label.config(image=frame.picture)
    else:
        frame.picture = tk.PhotoImage(file="C:/Users/matve-il/PycharmProjects/CoinFlip/eagle_res.PNG")
        frame.label.config(image=frame.picture)
    frame.label.after(3000, lambda: change_back())


def change_back():
    frame.picture = tk.PhotoImage(file="C:/Users/matve-il/PycharmProjects/CoinFlip/questionmark.PNG")
    frame.label.config(image=frame.picture)


frame = tk.Frame(root, borderwidth=2, bg="white", relief='groove')
frame.pack(side='top', fill="x")

frame.picture = tk.PhotoImage(file="C:/Users/matve-il/PycharmProjects/CoinFlip/questionmark.PNG")
frame.label = tk.Label(frame, image=frame.picture)
frame.label.pack()

flip_button = tk.Button(root, bd=5, bg='#D2D3D3', text='! FLIP !', command=coinflip)
flip_button.place(x=60, y=175)

root.mainloop()
