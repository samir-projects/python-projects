from survey import AnonymousSurvey

question= "What language did you first learn to speak"
language_survey=AnonymousSurvey(question)
language_survey.show_question()
print('Enter q to quit anytime')
while True:
    response= input("Language: ")
    if response=='q':
        break
    language_survey.store_responses(response)
language_survey.show_result()