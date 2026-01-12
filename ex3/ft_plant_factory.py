class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


plants_data = {
    "Rose": [25, 30],
    "Oak": [200, 365],
    "Cactus": [5, 90],
    "Sunflower": [80, 45],
    "Fern": [15, 120],
}
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
