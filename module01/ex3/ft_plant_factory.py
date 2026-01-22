#!/usr/bin/env python3
"""Plant factory system for creating and managing multiple plants."""


class Plant:
    """Blueprint for representing a plant with its attributes."""
    def __init__(self, name: str, height: int, age: int):
        """
         Initialize a new plant.

        Args:
            name (str): Name of the plant
            height (int): Height in centimeters
            age (int): Age in days
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """ Display the plant's current information."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


class PlantFactory:
    """Factory for creating and tracking plants."""
    def __init__(self):
        """Initialize the factory with an empty plant list and counter."""
        self.plants = []
        self.count = 0

    def create_plant(self, name: str, height: int, age: int):
        """Create a new plant and add it to the factory's collection."""
        plant = Plant(name, height, age)
        self.plants += [plant]
        self.count += 1


print("=== Plant Factory Output ===")
factory = PlantFactory()
factory.create_plant("Rose", 18, 17)
factory.create_plant("Sunflower", 17, 8)
factory.create_plant("Cactus", 18, 17)
factory.create_plant("Fern", 17, 8)
factory.create_plant("Oak", 107, 38)
for p in factory.plants:
    p.get_info()
print(f"Total plants created: {factory.count}")
