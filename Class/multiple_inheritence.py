class Vehicle:
    typebody = "truck"
    wheels = 12
    driver = 2

class Car(Vehicle):  # Changed the class name to follow Python naming conventions
    name = "EICHER"

class Driver(Car):  # Multiple inheritance with Vehicle and Car as base classes
    pass

#error may come of TypeError: Cannot create a consistent method resolution MRO
# Accessing attributes from base classes
print(Driver.typebody)  # Output: truck
print(Driver.driver)    # Output: 2