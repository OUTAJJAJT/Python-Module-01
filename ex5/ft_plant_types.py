"""
Plant Types Module

This module demonstrates inheritance with different plant types.
Each plant type has unique properties and behaviors.
"""


class Plant:
    """
    Base class representing a generic plant.
    """
    def __init__(self, name, height, age):
        """Initialize a Plant object."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flowering plant.
    Inherits from Plant and adds color and blooming capability.
    """
    def __init__(self, name, height, age, color):
        """Initialize a Flower object."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Display flowering plant information and blooming status."""
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.
              color} color")
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """
    Represents a tree plant.
    Inherits from Plant and adds trunk diameter and shade production.
    """
    def __init__(self, name, height, age, trunk_diameter):
        """Initialize a Tree object."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Display tree information and calculate shade area."""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.
              trunk_diameter}cm diameter")
        print(f"{self.name} provides {3.14*((self.height / 100) ** 2)} square \
meters of shade!\n")


class Vegetable(Plant):
    """
    Represents a vegetable plant.
    Inherits from Plant and adds harvest season and nutritional value.
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize a Vegetable object."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


print("=== Garden Plant Types: ===\n")
f1 = Flower("Rose", 25, 30, "Red")
f2 = Flower("Sunflower", 80, 45, "Yellow")
t1 = Tree("Oak", 500, 1825, 50)
t2 = Tree("Pine", 300, 1095, 30)
v1 = Vegetable("Carrot", 80, 90, "summer", "High in Vitamin A")
v2 = Vegetable("Lettuce", 30, 60, "spring", "Rich in Fiber")
f1.bloom()
f2.bloom()
t1.produce_shade()
t2.produce_shade()
print(f"{v1.name} (Vegetable): {v1.height}cm, {v1.age} days, {v1.
      harvest_season} harvest")
print(f"{v1.name} is {v1.nutritional_value}.")
print(f"\n{v2.name} (Vegetable): {v2.height}cm, {v2.age} days, {v2.
      harvest_season} harvest")

print(f"{v2.name} is {v2.nutritional_value}.")
