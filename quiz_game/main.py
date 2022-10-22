from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_object = Question(question['question'], question['correct_answer'])
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"your final score was: {quiz.score}/{quiz.question_number}")
