from tkinter import *
import json
import requests


def information():
    name = text.get()
    link = ("https://api.github.com/users/{name}")
    response = requests.get(link).json()
    keys = ['company', 'created_at', 'email', 'id', 'name', 'url']
    response_new = {}
    for i in keys:
        response_new[i] = response[i]
    with open('info.txt', 'w') as file:
        json.dump(response_new, file, indent=3)


window = Tk()
window.title('information')
window.geometry('355x400')
lbl = Label(window, text='name', width=30, height=1, font=45)
lbl.grid(row=0, column=1, padx=10)
text = Entry(window, width=20)
text.grid(column=1, row=1, pady=20)
button = Button(window, text='show info', width=30, height=1, command=information)
button.grid(row=3, column=1, pady=20)
window.mainloop()
