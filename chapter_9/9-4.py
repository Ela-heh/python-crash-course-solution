class Restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0


    def describe(self):
        print(f"The {self.name} restaurnt has {self.cuisine} foods")

    def customer(self,num):
        self.number_served = num
    
    def set (self):
        print(f"The number of customers have been served are {self.number_served}")

    def increment (self,add):
        self.number_served += add
        print(f"The total number has updted to {self.number_served}")

restaurant = Restaurant("Mahi khob" , "sea")
restaurant.describe()
restaurant.customer(21)
restaurant.set()
restaurant.increment(10)
restaurant.increment(20)