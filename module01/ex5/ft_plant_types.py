#!/usr/bin/env python3
"""Garden plant system with inheritance hierarchy for different plant types."""


class Plant:
    """Base class for all plants with protected attributes and validation."""
    def __init__(self, name: str, height: int, age: int):
        """ Initialize a plant with validation."""
        self.__name = name
        if height < 0:
            print(f"Invalid height: {height}. Reset to 0.")
            self.__height = 0
        else:
            self.__height = height
        if age < 0:
            print(f"Invalid age: {age}. Reset to 0.")
            self.__age = 0
        else:
            self.__age = age

    def get_info(self):
        """Get basic plant information."""
        return f"{self.__height}cm, {self.__age} days"


class Flower(Plant):
    """Flower plant with color attribute and blooming behavior."""
    def __init__(self, name: str, height: int, age: int, color: str):
        """Initialize a flower."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Display a blooming message for the flower."""
        print(f"{self._Plant__name} is blooming beautifully!")

    def get_info(self):
        """Display detailed flower information including color."""
        print(f"{self._Plant__name} (Flower)", end=':')
        print(f" {super().get_info()}, {self.color} color")


class Tree(Plant):
    """Tree plant with trunk diameter and shade production."""
    def __init__(self, name: str, height: int, age: int, td: int):
        """Initialize a tree."""
        super().__init__(name, height, age)
        self.td = td

    def produce_shade(self, size: int):
        """Display the shade area provided by the tree."""
        print(f"{self._Plant__name} provides {size} square meters of shade")

    def get_info(self):
        """Display detailed tree information including trunk diameter."""
        print(f"{self._Plant__name} (Tree)", end=':')
        print(f"{super().get_info()}, {self.td}cm diameter")


class Vegetable(Plant):
    """Vegetable plant with harvest season and nutritional information."""
    def __init__(
                self,
                name: str,
                height: int,
                age: int,
                harvest_season: str,
                nutritional_value: str,
            ):
        """Initialize a vegetable."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        """Display detailed vegetable information"""
        print(f"{self._Plant__name} (Vegetable)", end=':')
        print(f"{super().get_info()}, {self.harvest_season} harvest")
        print(f"{self._Plant__name} is rich {self.nutritional_value}")


print("=== Garden Plant Types ===")
tulip = Flower("Tulip", 18, 8, "white")
rose = Flower("Rose", 28, 2, "red")

tulip.get_info()
tulip.bloom()
rose.get_info()
rose.bloom()
print(" ")
oak = Tree("Oak", 18, 8, 2026)
arbre = Tree("Treee", 18, 8, 2026)
oak.get_info()
oak.produce_shade(78)
arbre.get_info()
arbre.produce_shade(78)
print(" ")
tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 40, 75, "Autumn", "vitamin A")
tomato.get_info()
carrot.get_info()
