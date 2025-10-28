class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} year\'s old')

    def speak(self):
        print("I don't know what to say")

class Cat(Pet): 
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def speak(self):
        print('Meow')
    def show(self):
        print(f'I am {self.name} and I am {self.age} year\'s old and I am {self.color}')

class Dog(Pet):
    def speak(self):
        print('Bark')
class Fish(Pet):
    pass

p=Pet('Tim',34)
p.show()
c=Cat('Tim',24,'brown')
c.speak()
c.show()
d=Dog('Fuche',54)
d.speak()
f=Fish('Nimo',34)
f.speak()
