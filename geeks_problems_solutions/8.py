'''
Find if the number is prime or not
'''

def find_prime(num):
    flag=False
    if num<1:
        print ('Not prime')

    elif num>1:
        for i in range (2,num):
            if num%i==0:
                flag=True

        if flag:
            print ('Not prime')
        else:
            print ('Prime')

find_prime(15)
