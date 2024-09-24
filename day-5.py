# Problem: Car Odometer

# Creating a Python class to model a car's odometer. The class should have the following functionality:

# Initialize a car with attributes for make, model, and year.
# Track the odometer reading, initially set to 0.
# Provide methods to retrieve and update the odometer reading.
# Ensure that the odometer reading cannot be rolled back to a lower value.

# Your task is to implement the Car class according to the given specifications and 
# demonstrate its usage by creating an instance of the Car class and performing the following actions:

# Print the car's make, model, and year.
# Print the initial odometer reading.
# Update the odometer reading to 100.
# Attempt to roll back the odometer reading to 50 (which should fail).
# Drive the car by 50 miles and print the updated odometer reading.

# Your solution should demonstrate proper encapsulation and adherence to OOP principles.

class Car:
    def __init__(self, make, model, year):
        self._odometer = 0
        self.car_make = make
        self.Car_model = model
        self.Car_year = year

    def get_car(self):
        return self.car_make,self.Car_model,self.Car_year

    def get_odometer(self):
        return self._odometer
    
    def car_drive(self,miles):
        self._odometer+=miles
        return f"Car drived {miles} miles"

    def update_odometer(self, odometer):
        if self._odometer > odometer: 
            return print("invalid value")
        self._odometer = odometer

Mycar = Car("tata","t20","2024")

print(Mycar.get_car())
print(Mycar.get_odometer())
print(Mycar.update_odometer(100))
print(Mycar.get_odometer())
print(Mycar.update_odometer(50))
print(Mycar.car_drive(50))
print(Mycar.get_odometer())



# Problem: Geometric Shapes

# Create a model geometric shapes using object-oriented programming. You are provided with an abstract class Shape,
# which defines two abstract methods: area() and perimeter(). You need to create concrete subclasses of Shape to represent 
# specific shapes and provide implementations for these methods.

# Your task is to:

# Implement the Rectangle class, a subclass of Shape, to represent rectangles. The Rectangle class should have attributes
#  for width and height, and it should provide methods to calculate the area and perimeter of a rectangle.

# Test the functionality of the Rectangle class by creating an instance of it with width 5 and height 4. 
# Calculate and print the area and perimeter of the rectangle.

# Your solution should demonstrate proper usage of abstract classes and methods, 
# as well as inheritance and method overriding in Python.
from abc import abstractmethod,ABC

class Shape(ABC):

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def area(self):
        return f"area is  {self.height * self.width}"
    
    def perimeter(self):
        return f"perimeter is  {2*(self.height + self.width)}"
    

rect = Rectangle(height=4,width=5)
print(rect.area())
print(rect.perimeter())


# decorator Problem

# creating a Python decorator that logs the time from start and end of the execution of a 
# function along with its arguments and return value. 

# Your task is to implement the log_decorator decorator function and apply it to the function 
# (create function of your choice).

# Your solution should demonstrate the usage of the log_decorator decorator to log the execution of the function.

# (Note log is just “Texts”)
import time

def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time() 
        add = func(*args,**kwargs)
        end_time = time.time()
        print(f"add function start at {start_time} and end at {end_time} and argument are {args},{kwargs} ")
        return add
    return wrapper

@execution_time
def addnum(x, y):
    return x + y

result = addnum(2, 3)
print(result)
