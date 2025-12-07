# a class is a blueprint for creating objects

class Dog:
    # class attribute
    species = "Canis familiaris"

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

poodle = Dog("Poodle", 3)
bulldog = Dog("Bulldog", 5)
print(poodle.description())

print(bulldog.speak("Woof"))

# INHERITANCE
# allows a class to inherit attributes and methods from another class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def description(self):
        return f"{self.make} {self.model}"

# Inheriting from Car class

class ElectricCar(Car):
    def __init__(self, make, model, battery_size=75):
        super().__init__(make, model)
        self.battery_size = battery_size

    def description(self):
        return f"{self.make} {self.model} with a {self.battery_size}-kWh battery"

audi = Car("Audi", "A4")
tesla = ElectricCar("Tesla", "Model S", 100)
print(audi.description())
print(tesla.description())

# multiple inheritance along with method overriding
# allows a class to inherit from multiple classes

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def description(self):
        return f"This vehicle has {self.wheels} wheels."

class Truck(Vehicle):
    def __init__(self, wheels, capacity):
        super().__init__(wheels)
        self.capacity = capacity

    def description(self):
        return f"This truck has {self.wheels} wheels and a capacity of {self.capacity} tons."

class ElectricTruck(Truck):
    def __init__(self, wheels, capacity, battery_size):
        super().__init__(wheels, capacity)
        self.battery_size = battery_size

    def description(self):
        return f"This electric truck has {self.wheels} wheels, a capacity of {self.capacity} tons, and a {self.battery_size}-kWh battery."

# Creating instances of the classes
vehicle = Vehicle(4)
truck = Truck(6, 10)
electric_truck = ElectricTruck(8, 15, 200)

print(vehicle.description())
print(truck.description())
print(electric_truck.description())

# polymorphism
# polymoprhism can be achieved by method overriding and interfaces

# method overriding is when a subclass provides a specific implementation of a method that is already defined in its superclass
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Cat(Animal):
    def speak(self):
        return "Meow"


class Dog(Animal):
    def speak(self):
        return "Woof"


cat = Cat()
dog = Dog()

print(cat.speak())  # Output: Meow
print(dog.speak())  # Output: Woof
# here polymorphism is achieved through method overriding, as both Cat and Dog classes implement the speak method in their own way

# polymorphism through functions and methods

class Shape:
    def area(self):
        return "the area of the figure"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# function that demonstrates polymorphism

def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")

# creating instances of the classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# calling the function with different shapes
print_area(circle)  # Output: The area of the shape is: 78.5
print_area(rectangle)  # Output: The area of the shape is: 24

# interfaces or abstract classes
# an interface is a contract that defines a set of methods that a class must implement
# in python, we can use abstract base classes (ABCs) to create interfaces
# ABCs are used to define common methods for a group of related classes
#  they can also be used to enforce a contract for subclasses to follow

from abc import ABC, abstractmethod

class Shape(ABC):
    # This is an abstract class that defines the interface for all shapes
    @abstractmethod
    def area_of_shape(self):
        pass

    @abstractmethod
    def perimeter_of_shape(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # implementing the abstract methods
    # if we don't implement these methods, we will get an error
    # when we try to create an instance of the Circle class    
    def area_of_shape(self):
        return 3.14 * self.radius * self.radius

    # this will throw an error
    #def perimeter_of_shape(self):
    #   return 2 * 3.14 * self.radius

# Encapsulation
# Encapsulation is the bundling of data(variables) and methods(functions) that operate on that data within a single unit, or class.

# It restricts direct access to some of an object's components and can prevent the accidental modification of data.
# It is achieved by using private and public access modifiers.

# Public, protected, and private access modifiers:

class Person:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self._age = age   # protected attribute can only be accessed within the class and its subclasses
        self.__ssn = "123-45-6789"  # private attribute (name mangling)

    def get_ssn(self):
        return self.__ssn  # public method to access private attribute

person = Person("John", 30)
print(person.name)  # Output: John (public attribute)
print(person.get_ssn())  # Output: 123-45-6789 (accessing private attribute through a public method)

# The private attribute __ssn cannot be accessed directly
print(person.__ssn)  # This will raise an AttributeError

# Encapsulation with getter and setter methods
# why getter and setter methods are used?
# They are used to control access to private attributes and provide a way to validate data before setting it.
# This is useful for maintaining data integrity and encapsulation.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def get_balance(self):
        return self.__balance  # getter method

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount  # setter method
        else:
            print("Invalid amount. Balance cannot be negative.")

account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
account.set_balance(2000)  # Setting a new balance
print(account.get_balance())  # Output: 2000

# In Python, we can use properties to create getter and setter methods in a more elegant way.
# Properties allow us to define methods that can be accessed like attributes, providing a clean interface for accessing and modifying private attributes.
# Properties are defined using the @property decorator for the getter method and the @<property_name>.setter decorator for the setter method.
# This allows us to define custom behavior when getting or setting the value of an attribute.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    @property
    def balance(self):
        return self.__balance  # getter method

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount  # setter method
        else:
            print("Invalid amount. Balance cannot be negative.")

account = BankAccount(1000)
print(account.balance)  # Output: 1000
account.balance = 2000  # Setting a new balance
print(account.balance)  # Output: 2000

# Abstraction
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.

from abc import ABC, abstractmethod

class Vechile(ABC):
    def drive(self):
        return "Driving the vehicle"

    @abstractmethod
    def fuel_efficiency(self):
        pass  # Abstract method, must be implemented by subclasses
    # how abstraction works here
    # The Vechile class is an abstract class that defines the interface for all vehicles.
    # It has a concrete method drive() that can be used by all subclasses, and an abstract method fuel_efficiency() that must be implemented by any subclass.
    # The subclasses Car and Truck inherit from the Vechile class and provide their own implementations of the fuel_efficiency() method.
    # This allows us to create different types of vehicles with their own specific behaviors while still adhering to the common interface defined by the Vechile class.

class Car(Vechile):
    def fuel_efficiency(self):
        return "Car fuel efficiency is 25 km/l"

class Truck(Vechile):
    def fuel_efficiency(self):
        return "Truck fuel efficiency is 10 km/l"

car = Car()
truck = Truck()

print(car.drive())  # Output: Driving the vehicle
print(car.fuel_efficiency())  # Output: Car fuel efficiency is 25 km/l
print(truck.drive())  # Output: Driving the vehicle
print(truck.fuel_efficiency())  # Output: Truck fuel efficiency is 10 km/l

# Magic methods
# Magic methods are special methods in Python that start and end with double underscores (__) and are used to define the behavior of objects in certain situations.
# They allow us to customize the behavior of built-in operations for our classes, such as addition, subtraction, string representation, and more.

# Eg: __init__, __str__, __repr__, __add__, __len__, etc.

class Point:
    pass

point = Point()

dir(point)
# The dir() function returns a list of the attributes and methods of the object.

# Basic magic methods

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): # String representation of the object
        return f"Point({self.x}, {self.y})"

    def __add__(self, other): # Overloading the + operator
        # operator overloading
        # allows us to define custom behavior for operators like +, -, *, /, etc.
        # when we use the + operator on two Point objects, it will call this method
        return Point(self.x + other.x, self.y + other.y)

    def __len__(self): # Length of the object (number of coordinates)
        return 2  # A point has two coordinates (x and y)

# Overloading operators for complex numbers

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):  # String representation of the complex number
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):  # Overloading the + operator for complex numbers
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):  # Overloading the - operator for complex numbers
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):  # Overloading the * operator for complex numbers
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)

c1= ComplexNumber(2, 3)
c2= ComplexNumber(4, 5)

print(c1)  # Output: 2 + 3i
print(c2)  # Output: 4 + 5i

c3 = c1 + c2  # Using the overloaded + operator
print(c3)  # Output: 6 + 8i

c4 = c1 - c2  # Using the overloaded - operator
print(c4)  # Output: -2 - 2i
