class User:
    def __init__(self,first_name,last_name,age,country,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.login_attempts=login_attempts
    def describe_user(self):
        print(f'{self.first_name}{self.last_name} is {self.age} year`s old. He is from {self.country}')
    def greet_user(self):
        print(f'Hi {self.first_name}')
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f'{self.login_attempts}')
    def reset_login_atttempts(self):
        self.login_attempts=0
        print(f'{self.login_attempts}')

user1=User('Samir','Sapkota',29,'Nepal',5)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.reset_login_atttempts()
