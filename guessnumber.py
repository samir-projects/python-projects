'''
This program is a simple game used to guess the number
'''
import random
import sys
num=random.randrange(1,10)
count=0
while count<3:
    prediction=int(input('Enter the predicted numer\n'))
    if (prediction==0):
        print('Enter the valid number between 1 and 10')
        sys.exit()
    if (prediction==num):
        print('Your prediction is correct')
        sys.exit()
    elif(prediction>num):
        print('Your prediction is greater than number')
    else:
        print('Your prediction is less than number')