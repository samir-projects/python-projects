class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_resturant(self):
        print(f'{self.resturant_name} {self.cuisine_type}')
    
    def open_resturant(self):
        print(f'{self.resturant_name} is open')

    def set_number_served(self,number_served):
        self.number_served=number_served
        print(f'{self.number_served}')

    def increment_number_served(self,increment_number):
        self.increment_number=increment_number
        self.increment_number=self.number_served+self.increment_number
        print(f'{self.increment_number}')

resturant=Resturant('Hayat','Italian')
resturant.set_number_served(26)
resturant.increment_number_served(30)


