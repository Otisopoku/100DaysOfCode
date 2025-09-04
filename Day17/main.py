from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_object = Question(questions["text"], questions["answer"])
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz"
      f"Your final score was {quiz.score}/{quiz.question_number}"
      )