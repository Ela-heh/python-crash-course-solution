class User:
    def __init__(self, first , last):
        self.fname = first
        self.lname = last
    
    def describe(self):
        print(f"The user's name is : \n{self.fname} {self.lname}")
    
    def greet(self):
        print(f"Greetings ,{self.fname}")

user1 = User('Mohammad Mahdi' , 'Khaligh')
user1.describe()
user1.greet()
