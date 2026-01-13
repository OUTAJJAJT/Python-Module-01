"""
Garden Plant Registry Module

This module creates a plant registry using classes to store plant information.
"""
print("=== Garden Plant Registry ===")


class Plant:
    """
    Represents a plant with basic attributes.
    Attributes:
        name (str): The name of the plant
        height (int): The height of the plant in centimeters
        age (int): The age of the plant in days
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


Rose = Plant("Rose", 25, 30)
Sunflower = Plant("Sunflower", 80, 45)
Cactus = Plant("Cactus", 15, 120)
plants = [Rose, Sunflower, Cactus]
for plant in plants:
    print(f"{plant.name}: {plant.height} cm, {plant.age} days old")
