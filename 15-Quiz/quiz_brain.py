class QuizBrain:
    def __init__(self , q_list):
        self.question_numbers = 0
        self.question_list = q_list
        self.score = 0





    def still_has_question(self):
        length_of_list = len(self.question_list)
        return self.question_numbers < length_of_list




    def next_question(self):

        curr_question = self.question_list[self.question_numbers]
        self.question_numbers+=1
        user_answer = input(f"Q.{self.question_numbers}:{curr_question.text} (True / False?)")

        self.check_answer(user_answer,curr_question.answer)



    def check_answer(self , user_answer , actual_answer):

        if user_answer.lower() == actual_answer.lower():
            self.score+=1
            print(f"you got right")


        else:
            print(f"wrong , the answer was {actual_answer}")
        print(f"score is {self.score}/{self.question_numbers}")
        print("\n")


