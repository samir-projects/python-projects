class Favourite:
    def __init__(self,question):
        self.question=question
        self.response=[]
    
    def display_question(self):
        print(self.question)

    def store_responses(self,new_response):
        self.response.append(new_response)
    
    def show_response(self):
        for response in self.response:
            print(f'{response}')

