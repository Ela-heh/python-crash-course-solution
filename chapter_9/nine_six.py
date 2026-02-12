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


class IceCreamStand(Restaurant):
    # 1. Update __init__ to accept arguments required by the Parent class
    def __init__(self, name, cuisine):
        # 2. Fix super() syntax and pass required arguments
        super().__init__(name, cuisine) 

    def flavor(self):
        icecream = ['chocklate','vanilla','safforn']
        for i in icecream:
            print(i)

'''stand = IceCreamStand("IceCreamStand", "Ice Cream")
stand.describe()
stand.flavor()'''