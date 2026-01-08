class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.height = 0
        self.age = 0
        print("Plant Created:", self.name)

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {self.age} days [OK]")

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height} cm [REJECTED]"
                  )
            print("Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {self.height} cm [OK]")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def get_info(self):
        print(f"\nCurrent plant: {self.name}({self.height}cm, {self.age} days)"
              )


print("=== Garden Security System ===")
plant = SecurePlant("Rose")
plant.set_height(25)
plant.set_age(30)
print()
plant.set_height(-5)
plant.get_info()
