class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print('Bark')
    
    @classmethod
    def tommy(cls):
        return Dog('Tommy',43)

dog=Dog.tommy()
print(dog.name)