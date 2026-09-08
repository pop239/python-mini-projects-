from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for q in question_data:
    # ques = Question(q["text"],q["answer"])
    # question_bank.append(ques)

    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_q = Question(question_text,question_answer)
    question_bank.append(new_q)



quiz = QuizBrain(question_bank)

while quiz.still_has_question():

    quiz.next_question()


print("you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_numbers}")