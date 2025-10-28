class Person:
    count=0

    def __init__(self,name):
        self.name=name
        Person.count+=1

p1=Person('Samir')
p2=Person('Savya')
p3=Person('Anita')
print(Person.count)