class Resturant:
    def __init__(self,resturant_name,cusine_type):
        self.resturant_name=resturant_name
        self.cusine_type=cusine_type
    def describe_resturant(self):
        print(f'The name of resturant is {self.resturant_name} and cusine type is {self.cusine_type}')
    def open_resturant(self):
        print('Resturant is open')

res1=Resturant('Solti','Nepali')
res1.describe_resturant()
res1.open_resturant()
res2=Resturant('Hayat','Chinese')
res2.describe_resturant()
res2.open_resturant()