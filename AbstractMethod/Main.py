#in there i call the object of the Abs2 file and call the method to display the details of the car and truck class which is inherited from the vehicle class and have the method to display the details of the vehicle class declaring by the for loop and creating the object of the car and truck class and calling
import Abs2 as Abs
import bank as bank
Car = Abs.Car
Bike = Abs.Bike
p=[Car,Bike]
for i in p:
    i.start()
    i.stop()
sbi = bank.saving_account
sbi.deposit(2000)
sbi.withdraw(1000)



    
