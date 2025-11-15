class User:
    def __init__(self,first_name,last_name,department,roll_number,age):
        self.first_name=first_name
        self.last_name=last_name
        self.department=department
        self.roll_number=roll_number
        self.age=age
        self.login_attempts=0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is enrolled in {self.department}. His roll number is {self.roll_number}. He is currently {self.age} year's old")

    def greet_user(self):
        print(f"Welcome to the group {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        print

user1=User('Samir','Sapkota', 'Elex','710413','29')
user2=User('Sudeep','Sharma', 'Elex','710414','30')
user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()