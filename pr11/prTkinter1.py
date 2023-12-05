import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import filedialog as fd


def equally():
    if combo.get() == '+':
        res = int(name.get()) + int(name1.get())
        lb1.configure(text=str(res))
    elif combo.get() == '-':
        res = int(name.get()) - int(name1.get())
        lb1.configure(text=str(res))
    elif combo.get() == '*':
        res = int(name.get()) * int(name1.get())
        lb1.configure(text=str(res))
    elif combo.get() == '/':
        res = int(name.get()) // int(name1.get())
        lb1.configure(text=str(res))


root = tk.Tk()
root.title('Лихотин Денис')
root.geometry('600x500+450+120')
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(pady=0, expand=True)

tab1 = ttk.Frame(notebook, width=600, height=500)
tab2 = ttk.Frame(notebook, width=600, height=500)
tab3 = ttk.Frame(notebook, width=600, height=500)

tab1.pack(fill='both', expand=True)
tab2.pack(fill='both', expand=True)
tab3.pack(fill='both', expand=True)

notebook.add(tab1, text='калькулятор')
notebook.add(tab2, text='чекбоксы')
notebook.add(tab3, text='работа с текстом')

name = tk.Entry(tab1, font=('Arial', 15), width=6)
name.grid(row=0, column=0)

name1 = tk.Entry(tab1, font=('Arial', 15), width=6)
name1.grid(row=0, column=2)

mat = ("+", "-", "*", "/")

combo = ttk.Combobox(tab1, width=6, values=mat)
combo.current(0)
combo.grid(row=0, column=1)

ttk.Button(tab1, text='=', width=6, command=equally).grid(row=0, column=3)

lb1 = ttk.Label(tab1, font=('Arial', 15), background='green', foreground='white', width=6)
lb1.grid(row=0, column=4)


def a():
    mbox.showinfo('informaton', 'вы выбрали первый вариант')


def b():
    mbox.showinfo('informaton', 'вы выбрали второй вариант')


def c():
    mbox.showinfo('informaton', 'вы выбрали третий вариант')


def show():
    if first_value.get() == 1:
        a()
    elif second_value.get() == 1:
        b()
    elif third_value.get() == 1:
        c()


first_value = tk.IntVar()
first_value.set(0)
second_value = tk.IntVar()
second_value.set(0)
third_value = tk.IntVar()
third_value.set(0)

btn1 = ttk.Checkbutton(tab2, text='первый',
                       variable=first_value,
                       offvalue=0,
                       onvalue=1
                       )
btn2 = ttk.Checkbutton(tab2, text='второй',
                       variable=second_value,
                       offvalue=0,
                       onvalue=1
                       )
btn3 = ttk.Checkbutton(tab2, text='третий',
                       variable=third_value,
                       offvalue=0,
                       onvalue=1
                       )

btn1.grid(row=0)
btn2.grid(row=1)
btn3.grid(row=2)

btni = ttk.Button(tab2, text='show', command=show)
btni.grid(row=3)


def open_file():
    filepath = fd.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", "end")
            text_editor.insert("1.0", text)


def save_file():
    filepath = fd.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", "end")
        with open(filepath, "w") as file:
            file.write(text)


text_editor = tk.Text(tab3)
text_editor.grid(column=0, columnspan=2, row=1)
open_button = ttk.Button(tab3, text="Открыть файл", command=open_file)
open_button.grid(column=0, row=0, sticky='nsew', padx=10)
save_button = ttk.Button(tab3, text="Сохранить файл", command=save_file)
save_button.grid(column=1, row=0, sticky='nsew', padx=10)

root.mainloop()
