

class QuizBrain:

    def __init__(self,question_list):
        self.question_number: int = 0
        self.questions_list: list = question_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right! Your score is {self.score}/{self.question_number}")
        else:
            print(f"That's wrong. Your score is {self.score}/{self.question_number}")
        print(f"The correct answer is {correct_answer}")
        print("\n")