class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        return f"Hi, this is {self.name}"

    @classmethod
    def create_anynonymous(cls):
        return Person('Samir',36)

person=Person.create_anynonymous()
print(person.name)