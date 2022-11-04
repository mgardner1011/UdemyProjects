from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    word_df = pd.read_csv('data/to_learn.csv')
except FileNotFoundError:
    word_df = pd.read_csv('data/french_words.csv')
to_learn = word_df.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


def remove_word():
    global to_learn
    to_learn.remove(current_card)
    learning_df = pd.DataFrame(to_learn)
    learning_df.to_csv('data/to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_word)
right_button.grid(column=1, row=1)

next_card()


window.mainloop()
