class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


Rose = plant("Rose", "25cm", "30 days")
Oak = plant("Oak", "200cm", "365 days")
Cactus = plant("Cactus", "5cm", "90 days")
Sunflower = plant("Sunflower", "80cm", "45 days")
Fern = plant("Fern", "15cm", "120 days")
plants = [Rose, Oak, Cactus, Sunflower, Fern]
print("=== Plant Factory Output ===")
for p in plants:
    print(f"Created: {p.name} ({p.height}, {p.age})")
print("\nTotal plants created: 5")
