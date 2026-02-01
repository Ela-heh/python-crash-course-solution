class Restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def described_restaurant(self):
        print(f"The Restaurant's name is {self.name} and it's famous for {self.type} cuisine ")

    def open_restaurant(self):
        print(f"Restaurant is open from 7 to 22")

restaurant1 = Restaurant('Mahi Khoob' , 'shrimp')
restaurant1.described_restaurant()
restaurant2 = Restaurant('Pizza2000','pizza')
restaurant2.described_restaurant()