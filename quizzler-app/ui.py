from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score_text = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width= 280,text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))


        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_img, highlightthickness=0, padx=20, pady=20, bd=0, command=self.correct_tick)
        self.right_button.grid(row=2, column=0)

        self.wrong_button = Button(image=wrong_img, highlightthickness=0, padx=20, pady=20, bd=0, command=self.wrong_tick)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def correct_tick(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def wrong_tick(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
            

