class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_age(self):
        print(f"{self.name} age is {self.age}")

d1=Dog('tommy',26)
d2=Dog('Jerry',24)
d1.get_age()
d2.get_age()