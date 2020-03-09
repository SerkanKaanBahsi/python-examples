# It just works look at c++ or java for this
class Car:
    def drive(self):
        print("Car can be driven")
    def need_fuel(self):
        print("Needs Fuel")
class Bike:
    def drive(self):
        print("Bike can be driven")
    def need_fuel(self):
        print("Does not need fuel")
def check_vehicle(vehicle):
    vehicle.drive()
    vehicle.need_fuel()

my_bike= Bike()
my_car = Car()
check_vehicle(my_bike)
check_vehicle(my_car)