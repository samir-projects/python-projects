'''
This program find compound interest of a program
'''
def amount(p,t,r):
    A=p*(((r/100) + 1)**t)
    CI=A-p
    return CI

CI=amount(100000,2,12)
print(int(CI))
        



