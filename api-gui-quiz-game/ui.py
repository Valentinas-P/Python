from tkinter import *
from quiz_brain import QuizBrain
import html

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")

class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("GUI QUIZ APP")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, text="This is where the \ntext will go", fill=THEME_COLOR,
                                            font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, borderwidth=0,
                                  command=self.tick_button)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, borderwidth=0,
                                   command=self.unknown_button)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=html.unescape(q_text))
        else:
            self.canvas.itemconfig(self.text, text="You have reached end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def tick_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def unknown_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        elif not is_right:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
