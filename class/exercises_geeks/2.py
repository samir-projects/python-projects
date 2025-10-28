'''
Exercise 2: Develop a class Calculator with methods to add and subtract two numbers.
'''
class Calculator:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

calc=Calculator()
print(calc.add(4,5))
print(calc.sub(4,5))