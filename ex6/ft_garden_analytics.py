# class Plant:
#     def __init__(self, name, height, age):
#         self.name = name
#         self.height = height
#         self.age = age


# class Garden:
#     def __init__(self, name):
#         self.name = name
#         self.plants = []

#     def add_plant(self, plant):
#         self.plants.append(plant)


# class GardenManager:
#     def __init__(self):
#         self.gardens = []

#     def add_garden(self, garden):
#         self.gardens.append(garden)

#     def help_plants_grow(self):
#         for garden in self.gardens:
#             for plant in garden.plants:
#                 plant.height += 1


# print("=== Garden Management System Demo ===")
# manager = GardenManager()
# garden = Garden("Alice")
# p1 = Plant("Oak Tree", 25, 30)
# p2 = Plant("Rose", 15, 120)
# p3 = Plant("Sunflower", 80, 45)
# garden.add_plant(p1)
# garden.add_plant(p2)
# garden.add_plant(p3)
# manager.add_garden(garden)

# print(f"Added {p1.name} to {garden.name}'s garden")
# print(f"Added {p2.name} to {garden.name}'s garden")
# print(f"Added {p3.name} to {garden.name}'s garden\n")
# print(f"{garden.name} is helping all plants grow...")
# print(f"{p1.name} grew {p1.height}cm")
# print(f"{p2.name} grew {p2.height}cm")
# print(f"{p3.name} grew {p3.height}cm\n")

# print(f"=== {garden.name} Garden Report ===")
# print("Plants in garden:")

# for plant in garden.plants:
#     print("-", plant.name, ":", plant.height, "cm", )


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_type(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = True

    def get_type(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_type(self):
        return "prize flowers"


class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def get_total_growth(self):
        return sum(plant.height for plant in self.plants) - (100 + 25 + 50)

    def get_plant_stats(self):
        regular = sum(1 for p in self.plants if p.get_type() == "regular")
        flowering = sum(1 for p in self.plants if p.get_type() == "flowering")
        prize = sum(1 for p in self.plants if p.get_type() == "prize flowers")
        return regular, flowering, prize

    def calculate_score(self):
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points * 10
        return score


class GardenManager:
    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        self.gardens.append(garden)

    def help_plants_grow(self):
        for garden in self.gardens:
            for plant in garden.plants:
                plant.height += 1

    def validate_heights(self):
        for garden in self.gardens:
            for plant in garden.plants:
                if plant.height <= 0:
                    return False
        return True

    def print_all_gardens_score(self):
        print("Garden Scores - ", end="")
        for garden in self.gardens:
            print(f"{garden.name}: {garden.calculate_score()}", end="")
            if garden != self.gardens[-1]:
                print(", ", end="")


print("=== Garden Management System Demo ===\n")
manager = GardenManager()

# Alice's Garden
garden_alice = Garden("Alice")
p1 = Plant("Oak Tree", 100, 30)
p2 = FloweringPlant("Rose", 25, 120, "red")
p3 = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
garden_alice.add_plant(p1)
garden_alice.add_plant(p2)
garden_alice.add_plant(p3)
manager.add_garden(garden_alice)

# Bob's Garden
garden_bob = Garden("Bob")
p4 = Plant("Maple", 40, 200)
p5 = FloweringPlant("Tulip", 20, 90, "pink")
garden_bob.add_plant(p4)
garden_bob.add_plant(p5)
manager.add_garden(garden_bob)

print(f"Added {p1.name} to {garden_alice.name}'s garden")
print(f"Added {p2.name} to {garden_alice.name}'s garden")
print(f"Added {p3.name} to {garden_alice.name}'s garden\n")

# Store original heights
original_heights = {
    p1.name: p1.height,
    p2.name: p2.height,
    p3.name: p3.height
}

print(f"{garden_alice.name} is helping all plants grow...")
manager.help_plants_grow()

print(f"{p1.name} grew {p1.height - original_heights[p1.name]}cm")
print(f"{p2.name} grew {p2.height - original_heights[p2.name]}cm")
print(f"{p3.name} grew {p3.height - original_heights[p3.name]}cm\n")

print(f"=== {garden_alice.name}'s Garden Report ===")
print("Plants in garden:")
for plant in garden_alice.plants:
    if isinstance(plant, PrizeFlower):
        print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (\
blooming), Prize points: {plant.prize_points}")
    elif isinstance(plant, FloweringPlant):
        print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (\
blooming)")
    else:
        print(f"- {plant.name}: {plant.height}cm")

print(f"\nPlants added: {len(garden_alice.plants)}, Total growth: \
{garden_alice.get_total_growth()}cm")

regular, flowering, prize = garden_alice.get_plant_stats()
print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize \
flowers")

print(f"\nHeight validation test: {manager.validate_heights()}")

manager.print_all_gardens_score()
print(f"\nTotal gardens managed: {len(manager.gardens)}")
