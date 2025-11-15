class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def update_odometer(self,odometer_reading):
        self.odometer_reading=odometer_reading

car=Car('audi','a4','2020')
car.update_odometer(56)