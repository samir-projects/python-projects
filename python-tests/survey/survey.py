class AnonymousSurvey:
    def __init__(self,questions):
        self.questions=questions
        self.responses=[]
    def show_question(self):
        print(self.questions)
    
    def store_responses(self,new_responses):
        self.responses.append(new_responses)

    def show_result(self):
        print("Survey Results")
        for responses in self.responses:
            print({responses})
