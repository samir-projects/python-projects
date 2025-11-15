class Fruits:
    def __init__(self,name,color,taste):
        self.name=name
        self.color=color
        self.taste=taste

class Apple(Fruits):
    def __init__(self,name,color,taste,price):
        super().__init__(name,color,taste)
        self.price=price

    def display_details(self):
        if self.price<100:
            print(f'{self.name} is expensive')
        print(f'{self.name} is cheap')

frt=Fruits('Apple','red','sweet')
app=Apple('Apple','red','sweet',1000)
app.display_details()