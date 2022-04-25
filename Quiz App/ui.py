from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Oswald', 12, "normal")

class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text= "Score: 0", bg= THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg= "white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text= "question", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        checkmark = PhotoImage(file="images/true.png")
        self.true_button = Button(image=checkmark, command=self.true)
        self.true_button.grid(row=2, column=0)
        x_mark = PhotoImage(file="images/false.png")
        self.false_button = Button(image=x_mark, command=self.false)
        self.false_button.grid(row=2, column=1)

        self.fetch_question()

        self.window.mainloop()

    def fetch_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text= "You did it bud. This is the end.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        self.check_correct(self.quiz.check_answer("True"))
    def false(self):
        self.check_correct(self.quiz.check_answer("False"))
    def check_correct(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.fetch_question)