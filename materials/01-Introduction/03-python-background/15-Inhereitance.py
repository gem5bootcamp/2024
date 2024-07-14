"""
This script the concept of class inheritance in Python.
"""

# In hereitance allows for a class to be defined in relation to another class.
# This other class is refered to as the base class, parent class, or super
# class. with the new class being the derived class, child class, or sub class.

# there are many instances where a new class is needed but shares amyn of the
# same attributes and methods as an existing class. In these cases it is
# possible to inherit from the existing class and extend it with new
# attributes and methods.

# Let's imagine we want to add an elephant object using  to our Animal class.
# We could want a new attribute "trunk_length" and a new method "trumpet".
# The insignt here is Elephants are Animals, but not all Animals are Elephants.
# An Elephant will always have all the common attributes and methods of an
# Animal, but not all Animals will have the attributes and methods of an
# Elephant.

class Animal:
    def __init__(self, weight, height, name):
        self.weight = weight
        self.height = height
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Elephant(Animal):
    def __init__(self, name, age, trunk_length):
        # Call the constructor of the parent class
        super().__init__(name, age)
        self.trunk_length = trunk_length

    def trumpet(self):
        print("Trumpeting")

# The Elephant class inherits from the Animal class. This means
# that the Elephant class has all the attributes and methods of the Animal
# class. Not only does this save a lot of typing and time by borrowing the
# attributes and methods of the Animal class, but it also makes the code more
# readable and maintainable.

# Of most importance, an elephant can be passed as an animal to any function
# So:

def print_animal(animal):
    print(f"Name: {animal.name}")
    print(f"Age: {animal.age}")
    animal.speak()

# We can pass an Elephant object to the print_animal function
dog = Animal("Dog", 10)
elephant = Elephant("Dumbo", 10, 3)
print_animal(elephant)
print_animal(dog)

# However a function that expects an Elephant object will not accept an Animal
# object. This is because an Elephant is an Animal, but an Animal is not an
# Elephant.

def toot_horn(elephant):
    elephant.trumpet()

# This will work
toot_horn(elephant)

# This will not work
toot_horn(dog)


# Finally subclasses can override methods of the parent class. This is useful
# when the method of the parent class does not make sense for the subclass.
# For example, the Elephant class could override the eat method of the Animal
# class to print a different message when an Elephant eats.

class Elephant(Animal):
    def __init__(self, name, age, trunk_length):
        super().__init__(name, age)
        self.trunk_length = trunk_length

    def trumpet(self):
        print("Trumpeting")

    def eat(self, food):
        print(f"{self.name} is eating {food} with its trunk")
