class Person:
    count=0
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        Person.count+=1

person1=Person('Samir',29,'Scarborough')
person2=Person('Gill',29,'BritishColumbia')
person3=Person('Jay',39,'Cambridge')
person4=Person('Harinwde',49,'BritishCKitchner')
print(Person.count)

