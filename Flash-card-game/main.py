import os
from tkinter import *
import pandas
import random
from gtts import gTTS
from playaudio import playaudio
timer = None
BG_COLOR = "#B1DDC6"
FONT = "Arial", 40, "italic"
TIMER_FONT = "Arial", 20, "italic"
to_learn = {}
current_card = {}
# ---------------------------- CHOOSE RANDOM WORD - PANDAS -------------------------------

try:
    data = pandas.read_csv("Data/words_to_learn.csv")
except FileNotFoundError:
    dataa = pandas.read_csv("Data/German-English - Sheet1.csv")
    to_learn = dataa.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(language_title, text="German", fill="black")
    canvas.itemconfig(language_word, text=current_card["German"], fill="black")
    window.after(100)
    count_down(3)
# ---------------------------- WHEN USER KNOWS THE WORD ---------------------------------


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    dataa = pandas.DataFrame(to_learn)
    dataa.to_csv("Data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- COUNT DOWN MECHANISM -------------------------------


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="")


def count_down(count):

    canvas.itemconfig(timer_text, text=count)
    if count > -1:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        reset_timer()
        canvas.itemconfig(language_title, text="English", fill="white")
        canvas.itemconfig(language_word, text=current_card["English"], fill="white")
        canvas.itemconfig(canvas_image, image=back_card)
        audio_output = gTTS(text=current_card["German"], lang="de")
        audio_output.save("german.word.mp3")
        playaudio("german.word.mp3", True)
        os.remove("german.word.mp3")

# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title("Flash-Card-Game")
window.config(pady=50, padx=50, bg=BG_COLOR)

canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
language_title = canvas.create_text(400, 150, text="", font=FONT)
language_word = canvas.create_text(400, 263, text="", font=FONT)
timer_text = canvas.create_text(750, 50, text="00:00", font=TIMER_FONT)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, bg=BG_COLOR, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(column=1, row=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, bg=BG_COLOR, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(column=0, row=2)

next_card()
count_down(3)

window.mainloop()