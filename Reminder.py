import time
import tkinter as tk
from tkinter import messagebox
from threading import Thread

root = tk.Tk()
root.title('')
root.geometry('140x40')
root.resizable(False, False)


def open_reminder_window():
    reminderWindow = tk.Toplevel()
    reminderWindow.title('')
    reminderWindow.geometry('150x105')
    reminderWindow.resizable(False, False)

    reminder_label = tk.Label(reminderWindow, text='О чем тебе напомнить?')
    reminder_label.place(x=5, y=5)

    reminder_entry = tk.Entry(reminderWindow, width=20)
    reminder_entry.focus_set()
    reminder_entry.place(x=5, y=30)

    timer_label = tk.Label(reminderWindow, text='Через сколько минут?')
    timer_label.place(x=5, y=50)

    timer_entry = tk.Entry(reminderWindow, width=5)
    timer_entry.insert(0, 5)
    timer_entry.place(x=5, y=75)

    def threading():
        t1 = Thread(target=set_reminder_command)
        t1.start()

    def set_reminder_command():
        topic = reminder_entry.get()
        time_till_call = int(timer_entry.get())
        time_till_call_sec = time_till_call*60
        reminderWindow.destroy()
        time.sleep(time_till_call_sec)
        messagebox.showinfo('Эй ты!', topic)

    set_button = tk.Button(reminderWindow, bd=5, bg='#D2D3D3', text='ЕСТЬ!', width=4, command=threading)
    set_button.place(x=50, y=70)


remind_button = tk.Button(root, bd=5, bg='#D2D3D3', text='! НАПОМНИ МНЕ !', command=open_reminder_window)
remind_button.place(x=8, y=5)


root.mainloop()
