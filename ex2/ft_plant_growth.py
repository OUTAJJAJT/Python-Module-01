class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height-1} cm, {self.age-1} days old"

    def new_info(self):
        self.height += 1
        self.age += 1


Rose = Plant("Rose", 25, 30)
Sunflower = Plant("Sunflower", 80, 45)
Cactus = Plant("Cactus", 15, 120)
Plants = [Rose, Sunflower, Cactus]

start_heights = {plant.name: plant.height for plant in Plants}
target_plant = "Rose"
for day in range(1, 8):
    if day == 1 or day == 7:
        print(f"=== Day {day} ===")
        for plant in Plants:
            plant.new_info()
            if plant.name == target_plant:
                print(plant.get_info())
    else:
        for plant in Plants:
            plant.new_info()

print("Growth this week:", end="")
for plant in Plants:
    if plant.name == target_plant:
        new_height = plant.height - start_heights[plant.name] - 1
        print(f"+{new_height}cm")
