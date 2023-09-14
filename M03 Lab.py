
'''
Savana Fallen
10/09/2023
M03 Lab.py
Desc: This application accepts the users input for the various attiributes of a vehicle, assigns those attributes to a class, and then prints those attributes for the user to see.
'''
#Parent class
class Vehicle:
    #assigns users input to vehicle_type
    def __init__(self):
        self.vehicle_type = input("Enter vehicle type: ")

#Child class which inherits the attributes from its parent class
class Automobile(Vehicle):

    #Creates a function which takes and assigns the users input to the year, make, model, doors, and roof attributes
    def attributes(self):
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")

        self.doors = input("Enter door count (can be 2 or 4): ")
        #Checks whether the user has entered 2 or 4 for the self.doors attribute. If not it keeps looping until they do.
        while self.doors != "2" and self.doors != "4":
            self.doors = input("Sorry that answer is not valid. Please re-enter the door count (can be 2 or 4): ")
            if self.doors == "2" or self.doors == "4":
                break
        
        self.roof = input("Enter the type of roof (solid roof or sun roof: ")
        #Checks whether the user has entered solid roof or sun roof for the self.roof attribute. If not keeps looping until they do.
        while self.roof != "solid roof" and self.roof != "sun roof":
            self.roof = input("Sorry that answer is not valid. Please re-enter the type of roof (may be solid roof or sun roof): ")
            if self.roof == "solid roof" or self.roof == "sun roof":
                break

    #creates a function which prints all of the attributes that we got from the user.
    def show(self):
        print(f'\nVehicle type: {self.vehicle_type} \nYear: {self.year} \nMake: {self.make} \nModel: {self.model} \nNumber of doors: {self.doors} \nType of roof: {self.roof}')

#Stores the Automobile class as a variable
obj = Automobile()

#Calls the 'this' function as well as the 'show' function from the Automobile class
obj.attributes()
obj.show()


