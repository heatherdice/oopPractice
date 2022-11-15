# Exercise 1: create vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Exercise 2: create vehicle class without any variables and methods
class Vehicle:
        pass

# Exercise 3: create child class Bus that will inherit all of the variables & methods of
# the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus('School bus', 180, 12)
print("Vehicle Name: ", School_bus.name, "Speed: ", School_bus.max_speed, "Mileage: ", School_bus.mileage)

# Exercise 4: Create a Bus class that inherits from the Vehicle class.
# Give capacity argument of Bus.seating_capacity() a default of 50.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus('School bus', 180, 12)
print(School_bus.seating_capacity())

# Exercise 5: Define a class attribute "color" with a default value white.
# I.e., every Vehicle should be white.
class Vehicle:
    color = 'white' # class variable shared between all instances, subclasses, therefore defined outside constructor
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Exercise 6: Create a Bus child class that inherits from the Vehicle class.
# Default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, add extra 10% on full fare as maintenance charge.
# Total fare for Bus will become final amount = total fare + 10% of total fare.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super.fare()
        amount += amount * 10/100
        return amount

School_bus = Bus("School bus", 12, 50)
print("Total bus fare is:", School_bus.fare())

# Exercise 7: Determine which class a given Bus object belongs to.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus('School bus', 12, 50)
print(type(School_bus))

# Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus('School bus', 12, 50)
print(isinstance(School_bus, Vehicle))
