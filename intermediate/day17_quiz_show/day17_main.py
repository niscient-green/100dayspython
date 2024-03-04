# Import data
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create and fill the question bank
question_bank = []
for i in question_data:
    new_question = Question(i["question"], i["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
