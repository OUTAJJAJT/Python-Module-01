"""
Garden Security System Module

This module implements data protection using properties and validation.
"""


class SecurePlant:
    """
    Represents a plant with protected data and validation.
    Data is protected using private attributes and properties with setters
    that validate values before assignment.
    """
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0
        print("Plant Created:", self.name)

    @property
    def height(self):
        """
        Get the plant height.
        Returns:
            int: The height in cm
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the plant height with validation.
        Only positive values are accepted. Negative values are rejected.
        Args:
            value (int): The height in cm
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value} cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {self.__height} cm [OK]")

    def set_height(self, value):
        """
        Set the plant height using property setter.
        Args:
            value (int): The height in cm
        """
        self.height = value

    def get_height(self):
        """
        Get the plant height.
        Returns:
            int: The height in cm
        """
        return self.height

    @property
    def age(self):
        """
        Get the plant age.
        Returns:
            int: The age in days
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        Set the plant age with validation.
        Only positive values are accepted. Negative values are rejected.
        Args:
            value (int): The age in days
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")

    def set_age(self, value):
        """Set the plant age using property setter."""
        self.age = value

    def get_age(self):
        """Get the plant age."""
        return self.age

    def get_info(self):
        """
        Print the current plant information.
        Displays the plant name, height, and age.
        """
        print(f"\nCurrent plant: {self.name}({self.__height}cm, {self.__age} \
days)")


print("=== Garden Security System ===")
plant = SecurePlant("Rose")
plant.set_height(30)
plant.set_age(10)
print()
plant.height = -5
plant.age = -10
print()
plant.get_info()
