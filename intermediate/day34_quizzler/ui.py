from tkinter import *
from quiz_brain import QuizBrain

# Set globals, constants --------------------------------------------------------------------------
BLUE = "#375362"
WHITE = "white"
GREEN = "green"
RED = "red"
FONT = ("Arial", 20, "italic")
PADDING = 20
QBOX_HEIGHT = 250
QBOX_WIDTH = 300


# Create UI for Quizzler game ---------------------------------------------------------------------
class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=PADDING, pady=PADDING, bg=BLUE)

        # Create canvas
        self.qbox_canvas = Canvas(width=QBOX_WIDTH, height=QBOX_HEIGHT, bg=WHITE)
        self.qbox_canvas.grid(row=1, column=0, columnspan=2, pady=PADDING)

        # Create labels
        self.score_label = Label(text="Score: 0", bg=BLUE, fg=WHITE, font=FONT)
        self.score_label.grid(row=0, column=1, pady=PADDING)
        self.question_label = self.qbox_canvas.create_text(
            QBOX_WIDTH / 2,
            QBOX_HEIGHT / 2,
            text="",
            font=FONT,
            fill=BLUE,
            width=QBOX_WIDTH - 20
        )

        # Create buttons
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.check_is_false,
        )
        self.false_button.grid(row=2, column=0, pady=PADDING)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.check_is_true,
        )
        self.true_button.grid(row=2, column=1, pady=PADDING)

        self.get_next_question()

        # Run window loop
        self.window.mainloop()

    def get_next_question(self):
        self.qbox_canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.qbox_canvas.itemconfig(self.question_label, text=question_text)
        else:
            self.qbox_canvas.itemconfig(self.question_label, text="End of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")


    def check_is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.get_next_question()

    def check_is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.get_next_question()

    def give_feedback(self, is_right: bool):
        if is_right:
            self.qbox_canvas.config(bg=GREEN)
        else:
            self.qbox_canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question())
