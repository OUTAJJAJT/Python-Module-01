"""
Plant Factory Module

This module creates multiple plant objects from a data dictionary.
"""


class Plant:
    """
    Represents a plant with name, height, and age.
    Attributes:
        name (str): The name of the plant
        height (int): The height of the plant
        age (int): The age of the plant
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


# Plant data dictionary
plants_data = {
    "Rose": [25, 30],
    "Oak": [200, 365],
    "Cactus": [5, 90],
    "Sunflower": [80, 45],
    "Fern": [15, 120],
}
# Create plant objects from dictionary data
plants = []
for name in plants_data:
    height, age = plants_data[name]
    plants.append(Plant(name, height, age))
print("=== Plant Factory Output ===")
i = 0
for p in plants:
    print(f"Created: {p.name} ({p.height} cm, {p.age} days)")
    i += 1
print(f"\nTotal plants created: {i} ")
