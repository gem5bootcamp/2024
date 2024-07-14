"""
This script demonstrates Abstract classes in Python and how they can be
inherited from to create new classes.
"""

# In the past couple of exmaples we've envisioned a simple class `Animal` that
# has object instantiations. There are cases where you don't want there to be
# any object instantiations of a class. This is where Abstract Base Classes.
# In our case it makes no sense to have a generic Animal when we can create a subclass for each animal type.
# Beyond this there could be enver more niche specialized subclasses for each animal type.

# Abstract Base Classes are classes that are meant to be inherited from, but not
# instantiated. They are used to define a common interface for subclasses to
# implement.

# The `abc` module in Python provides the `ABC` class that can be inherited from
# to create an Abstract Base Class.
# Methods do not have to be implemented in the Abstract Base Class, but they can
# be. This is useful for cases where you wish to enforce that a method is
# implemented in the subclass.

# Let's recreate an Animal class using an Abstract Base Class.

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    An abstract class that represents an animal.
    """

    @abstractmethod
    def eat(self, food):
        raise NotImplementedError("eat method not implemented")

    @abstractmethod
    def move(self):
        raise NotImplementedError("move method not implemented")


# We can then add animals. Let's say a Dog and a Cat:

class Dog(Animal):
    def eat(self, food):
        print(f"Dog is eating {food}")

    def move(self):
        print("Dog is walking")

class Cat(Animal):
    def eat(self, food):
        print(f"Cat is eating {food}")

    def move(self):
        print("Cat is walking")

# All we needed to do was specify the unimethods of the Animal class in the
# subclasses. We could add a subclass to cat. Let's say "LazyCat", which has
# a new method "sleep", unique to it while sharing all other Cat methods.

class LazyCat(Cat):
    def sleep(self):
        print("Cat is sleeping")

# WE can instantiate these classes and call their methods, everything except
# the abstract base class.

dog = Dog()
cat = Cat()
lazy_cat = LazyCat()

dog.eat("meat")
dog.move()

cat.eat("fish")
cat.move()

lazy_cat.eat("milk")
lazy_cat.move()
lazy_cat.sleep()
