
class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0
        print("Plant Created:", self.name)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value} cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {self.__height} cm [OK]")

    def set_height(self, value):
        self.height = value

    def get_height(self):
        return self.height

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")

    def set_age(self, value):
        self.age = value

    def get_age(self):
        return self.age

    def get_info(self):
        print(f"\nCurrent plant: {self.name}({self.__height}cm, {self.__age} \
days)")


print("=== Garden Security System ===")
plant = SecurePlant("Rose")
plant.set_height(25)
plant.set_age(10)
print()
plant.height = -5
plant.age = -10
print()
plant.get_info()
