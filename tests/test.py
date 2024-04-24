
from collections import Counter
# 1 ---

# Define a class named `Car`.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


# The constructor of this class should take two parameters: `make` (string) and `model` (string).
 
# 2 ---

# Create a class called `Dealership`.
class Dealership:
    def __init__(self):
        self.cars = []

# In the constructor, initialize an empty list named `cars` to store car instances.
 
# 3 ---

# Implement a method named `add_car` within the `Dealership` class.
    def add_car(self,car):
        if car.make and car.model:
            self.cars.append(car)
        
# This method should accept a single parameter `car`.

# The method should add the given car to the `cars` list but only if make and model aren't empty.
 
# 4 ---

# Add a method named `count_cars_by_make` to the `Dealership` class.
    def count_cars_by_make(self):
        car_makes = [car.make for car in self.cars]
        car_counts = Counter(car_makes)
        # car_counts = {}
        # for car in self.cars:
        #     car_counts[car.make] = car_counts.get(car.make, 0) + 1

        return car_counts

# This method should return a dictionary that shows the count of cars grouped by their respective makes.
 
# 5 ---

# Create a subclass named `LuxuryDealership`, inheriting from the `Dealership` class.
class LuxuryDealership(Dealership):
    def add_car(self, car):
        luxury_brand =  ["Mercedes", "BMW"]
        for car.make in luxury_brand:
            self.cars.append(car)

# Override the `add_car` method in the `LuxuryDealership` class.

# Modify the method to add cars only if their make is a luxury brand (e.g., "Mercedes", "BMW").
    
# 6 ---

# Create instances of the `Car` class with makes ("Toyota", "Toyota", "Mercedes", "BMW"),

cars = [
    Car("Toyota", "Camry"),
    Car("Toyota", "F-150"),
    Car("Mercedes", "E-class"),
    Car("BMW", "M5")
        ]
# and models ("Camry", "F-150", "E-Class", "M5").


# Ensure that the makes and models are provided as strings.

# Instantiate objects of both the `Dealership` class and the `LuxuryDealership` class.
dealership = Dealership()
luxurydealership = LuxuryDealership()
# Add all cars to each of these objects.
for car in cars:
    dealership.add_car(car)
    luxurydealership.add_car(car)


# Display the results of calling the `count_cars_by_make` method on both objects.
print("Dealership cars by count", dealership.count_cars_by_make())
print("Luxury cars by count", luxurydealership.count_cars_by_make())