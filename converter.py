from tkinter import *


def convert():
    miles = float(entry.get())
    km = round(miles * 1.609, 2)
    conversion_label.config(text=f'{km}')


window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

mi_label = Label(text='Mile(s)')
mi_label.grid(column=2, row=0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

conversion_label = Label(text='0')
conversion_label.grid(column=1, row=1)

entry = Entry(width=10)
entry.grid(column=1, row=0)

button = Button(text='Calculate', command=convert)
button.grid(column=1, row=2)
window.mainloop()
