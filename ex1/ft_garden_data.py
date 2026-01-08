print("=== Garden Plant Registry ===")


class Plant:
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
