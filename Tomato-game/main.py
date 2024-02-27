from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():

    canvas.itemconfig(work_text, text="Timer", fill=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        canvas.itemconfig(work_text, text="Work", fill=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        canvas.itemconfig(work_text, text="Break", fill=RED)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        canvas.itemconfig(work_text, text="Break", fill=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamidoras")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=220, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 170, image=tomato_img)
timer_text = canvas.create_text(100, 180, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

work_text = canvas.create_text(100, 30, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)
#
#
start_button = Button(text="Start", font=(FONT_NAME, 8, "bold"), command=start_timer)
start_button.grid(column=0, row=3)
#
check_label = Label(font=(FONT_NAME, 8, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 8, "bold"), command=reset_timer)
reset_button.grid(column=2, row=3)
#
window.mainloop()