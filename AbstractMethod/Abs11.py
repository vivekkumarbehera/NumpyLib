from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        print("Vehicle stopped.")
class Car(vehicle):
    def start(self):
        print("Car started.")
class Bike(vehicle):
    def start(self):
        print("Bike started.")
car = Car()
car.start()
car.stop()
bike = Bike()
bike.start()
bike.stop()