class Restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def described_restaurant(self):
        print(f"The Restaurant's name is {self.name} and it has {self.type} cuisine ")

    def open_restaurant(self):
        print(f"Restaurant is open from 7 to 22")

my_restaurant = Restaurant('Mahi Khoob' , 'shrimp')
my_restaurant.described_restaurant()
my_restaurant.open_restaurant()