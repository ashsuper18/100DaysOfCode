class QuizBrain:
    def __init__(self,qlist):
        self.quiz_number = 0
        self.score = 0
        self.question_list = qlist
    
    def still_has_question(self):
        return self.quiz_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.quiz_number]
        self.quiz_number+=1
        useranswer = input(
            f"Q.{self.quiz_number}: {current_question.text}. (True/False)?: ")
        self.check_answer(useranswer,current_question.answer)
    
    def check_answer(self,useranswer,correctans):
        if correctans.lower() == useranswer.lower():
            self.score +=1
            print(f"You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer is {correctans}.")
        print(f"Your current score is : {self.score}/{self.quiz_number}\n")


        
