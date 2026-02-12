class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_name(self):
        longname = f"{self.make} {self.model} {self.year}"
        return longname.title()
    
    def read_odometr(self):
        print (f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else :
            print("U can't roll back odometer!")

    def increment(self,miles):
        self.odometer_reading += miles

'''my_car = Car('audi','a40','2024')
print(my_car.get_name())
my_car.update_odometer(23_700)
my_car.increment(100)
my_car.read_odometr()
my_car.increment(-100)
my_car.read_odometr()'''