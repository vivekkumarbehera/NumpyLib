#There Have the Vechicle class and the Car class which is inherited from bike class,car class have the method which is used to display the details of the car and bike class and truck class which is inherited from bike class and have the method to display the details of the truck and bike class declaring by the for loop and creating the object of the car and truck class and calling the method to display the details of the car and truck.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_vehicle_info(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Vehicle Model: {self.model}")
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_car_info(self):
        self.display_vehicle_info()
        print(f"Number of Doors: {self.num_doors}")
class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)
        self.payload_capacity = payload_capacity

    def display_truck_info(self):
        self.display_vehicle_info()
        print(f"Payload Capacity: {self.payload_capacity} tons")
car = Car("Toyota", "Camry", 4)
truck = Truck("Ford", "F-150", 1.5)
p=[car,truck]
for i in p:
    i.display_vehicle_info()
    print()
    