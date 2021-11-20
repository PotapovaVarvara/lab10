# 7. Напишите программу на python, макет которой представлен ниже. При нажатии на
# кнопку “Включить”, синие круги превращаются в красные квадраты. Использовать модуль
# Tkinter.

from tkinter import *
root = Tk()
root.title("Лабораторная работа")
root.geometry("800x500")
canvas = Canvas(root, width = 800, height = 150, bg = 'white')
canvas.pack()
oval1 = canvas.create_oval(50, 10, 150, 110, width=2, fill = "blue")
oval2 = canvas.create_oval(650, 10, 750, 110, width=2, fill = "blue")
direction = 1


def start():
    canvas.itemconfig(oval1, fill='white')
    canvas.itemconfig(oval2, fill='white')

    rectangle1 = canvas.create_rectangle(50, 10, 150, 110, fill="red")
    rectangle2 = canvas.create_rectangle(650, 10, 750, 110, fill="red")


btn_convert = Button(text = "Включить", command = start)
btn_convert.pack()
root.mainloop()