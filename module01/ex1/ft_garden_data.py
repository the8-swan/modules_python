#!/usr/bin/env python3
"""Manage multiple plants in a community garden using a Plant class."""


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


rose = Plant("Rose", 18, 10)
sunflower = Plant("Sunflower", 17, 8)
tulip = Plant("tulip", 22, 19)
print("=== Garden Plant Registry ===")
print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
print(f"{tulip.name}: {tulip.height}cm, {tulip.age} days old")
