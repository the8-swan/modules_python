#!/usr/bin/env python3
"""Simulate plant growth over time with methods to modify plant state."""


class Plant:
    """Blueprint for representing a plant with methods to modify plant state"""

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

    def grow(self):
        """Increase the plant's height"""
        self.height += 1

    def add_age(self):
        """Increase the plant's age by one day."""
        self.age += 1

    def get_info(self):
        """ Return the plant's current information."""
        print(f"{self.name} : {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    """Main entry point: simulate a week of growth for multiple plants."""
tulip = Plant("Tulip", 22, 19)
rose = Plant("Rose", 25, 30)

counter = 0
print("=== Day 1 ===")
tulip.get_info()
rose.get_info()
print("=== Day 7 ===")
for counter in range(6):
    tulip.grow()
    tulip.add_age()
    rose.grow()
    rose.add_age()
    counter += 1
tulip.get_info()
rose.get_info()
print(f"Growth this week: +{counter}cm")
