'''
This program finds the simple interst of an amount
'''

def si(p,t,r):
    i=(p*t*r)/100
    return i
interest=si(100000,2,12)
print('Total interest is',interest)
