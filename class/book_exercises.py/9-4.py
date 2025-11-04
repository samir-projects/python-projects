class Resturant:
    def __init__(self,resturant_name,cusine_type):
        self.resturant_name=resturant_name
        self.cusine_type=cusine_type
        self.number_served=0
    def describe_resturant(self):
        print(f'The name of resturant is {self.resturant_name} and cusine type is {self.cusine_type}')
    def open_resturant(self):
        print('Resturant is open')
    def set_number_served(self,number_served):
        self.number_served=number_served
        print(f'The number of customers served are {self.number_served}')
    def increment_number_served(self,increment_number):
        self.increment_number=self.number_served+increment_number
        print(f'The number of customers served are {self.increment_number}')

res1=Resturant('Solti','Nepali')
res1.describe_resturant()
res1.open_resturant()
res1.set_number_served(30)
res1.increment_number_served(50)
res2=Resturant('Hayat','Chinese')
res2.describe_resturant()
res2.open_resturant()
res2.set_number_served(10)