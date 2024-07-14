"""
This script shows the basic principles behind creation classes and instantiaion
of objects from them.
"""

# Classes allow you to create your own data types in Python. They are a way to
# bundle data and functionality together in a single unit.
# A `class` is a blueprint for an object. It defines the attributes and methods
# object instances of the class will have.
# For example, we can have class `Car` with attributes like `color`, `make`,
# `model`, and methods like `drive`, `stop`, `park`. When we create an object
# of the class `Car`, we can set the attributes of the car object like `color`,
# `make`, `model` and call the methods like `drive`, `stop`, `park`. Though
# each objecct of the class `Car` will have the same attributes and methods,
# the values of the attributes can be different for each object.
#
# Object-oriented design is useful at many levels of software development. In
# gem5, the entire simulation is built around the concept of objects that are
# connected together and ultimately define the simulation.


# Here's an example of a simple class definition for an animal.
# It has properties: weight, height, name and methods eat, sleep.

class Animal:
    def __init__(self, weight, height, name):
        self.weight = weight
        self.height = height
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")

    def sleep(self):
        print(f"{self.name} is sleeping")

# To create an object of the class `Animal`, we call the class with the
# properties of the object as arguments. The class returns an object of the
# class `Animal` with the properties set to the values provided as arguments.
# Here we create two objects of the class `Animal` with the properties set to
# the values provided as arguments.
dog = Animal(100, 5, "Dog")
cat = Animal(200, 6, "Cat")

# We can access the properties of the object using the `.` operator.
print(f"Name of animal: {dog.name}")
print(f"Height of animal: {dog.height}")
print(f"Weight of animal: {dog.weight}")

# We can call the methods of the object using the `.` operator.
dog.eat("meat")
dog.sleep()

#These animals are the same type of object, even though they have different
# values for their properties. This allows for us to spediry APIs which accept
# an object of the class `Animal` and work with any object of the class `Animal`.

def feed_animal(animal):
    animal.eat("food")

feed_animal(dog)
feed_animal(cat)
