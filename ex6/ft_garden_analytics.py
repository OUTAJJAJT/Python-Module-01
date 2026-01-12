class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @staticmethod
    def get_type():
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    @staticmethod
    def get_type():
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    @staticmethod
    def get_type():
        return "prize flowers"


class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    @staticmethod
    def calculate_growth(current_height, initial_height):
        return current_height - initial_height

    def get_total_growth(self):
        total = 0
        for plant in self.plants:
            total += Garden.calculate_growth(plant.height, 100)
        return total

    def get_plant_stats(self):
        regular = 0
        flowering = 0
        prize = 0
        for plant in self.plants:
            if plant.get_type() == "regular":
                regular += 1
            elif plant.get_type() == "flowering":
                flowering += 1
            elif plant.get_type() == "prize flowers":
                prize += 1
        return regular, flowering, prize

    def calculate_score(self):
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points * 4
        return score


class GardenManager:
    @classmethod
    def validate_all_heights(cls, gardens):
        for garden in gardens:
            for plant in garden.plants:
                if plant.height <= 0:
                    return False
        return True

    @staticmethod
    def help_plants_grow(gardens):
        for garden in gardens:
            for plant in garden.plants:
                plant.height += 1

    @staticmethod
    def print_all_gardens_score(gardens):
        print("Garden Scores - ", end="")
        scores = []
        for garden in gardens:
            scores.append(f"{garden.name}: {garden.calculate_score()}")
        print(", ".join(scores))


print("=== Garden Management System Demo ===\n")

# Alice's Garden
garden_alice = Garden("Alice")
p1 = Plant("Oak Tree", 100)
p2 = FloweringPlant("Rose", 25, "red")
p3 = PrizeFlower("Sunflower", 50, "yellow", 10)
garden_alice.add_plant(p1)
garden_alice.add_plant(p2)
garden_alice.add_plant(p3)

# Bob's Garden
garden_bob = Garden("Bob")
p4 = Plant("Maple", 10)
p5 = FloweringPlant("Tulip", 25, "pink")
p6 = PrizeFlower("Sunflower", 14, "yellow", 10)
garden_bob.add_plant(p4)
garden_bob.add_plant(p5)
garden_bob.add_plant(p6)

gardens = [garden_alice, garden_bob]

print(f"Added {p1.name} to {garden_alice.name}'s garden")
print(f"Added {p2.name} to {garden_alice.name}'s garden")
print(f"Added {p3.name} to {garden_alice.name}'s garden\n")

original_heights = {
    p1.name: p1.height,
    p2.name: p2.height,
    p3.name: p3.height
}

print(f"{garden_alice.name} is helping all plants grow...")
GardenManager.help_plants_grow(gardens)

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

print(f"\nHeight validation test: \
{GardenManager.validate_all_heights(gardens)}")

GardenManager.print_all_gardens_score(gardens)
print(f"\nTotal gardens managed: {len(gardens)}")
