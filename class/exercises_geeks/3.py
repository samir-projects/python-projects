'''
Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways.
'''
class Employee:
    def __init__(self,name,age,department,id):
        self.name=name
        self.age=age
        self.department=department
        self.id=id
    
    def display_details(self):
        if self.name and self.age and self.department and self.id:
            print(f'{self.name} is {self.age} year\'s old. He works at {self.department} and his id number is {self.id}')


emp1=Employee('Samir',29,'Automation','TN30')
emp2=Employee('Anita',28,'Nurse','TN31')
emp1.display_details()
emp2.display_details()