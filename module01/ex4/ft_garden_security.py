#!/usr/bin/env python3
"""Secure plant system with data validation and encapsulation."""


class SecurePlant:
    """Plant class with protected attributes and data validation."""
    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a secure plant with validation.

        Args:
            name (str): Name of the plant
            height (int): Height in centimeters (negative values reset to 0)
            age (int): Age in days (negative values reset to 0)
        """
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
        print(f"Plant created: {name}")

    def set_height(self, height: int):
        """ Set plant height with validation."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.__height} cm [OK]")

    def set_age(self, age: int):
        """Set plant age with validation."""
        if age < 0:
            print(f"Invalid operation attempted: height {age}days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated:{self.__age} days [OK]")

    def get_height(self):
        """Get the plant's height."""
        return self.__height

    def get_age(self):
        """Get the plant's age."""
        return self.__age

    def get_info(self):
        """Display the plant's current information."""
        print(f"plant: {self.__name} ({self.__height}cm,{self.__age} days)")


def main():
    """Main function: demonstrate secure plant with validation."""
    print("=== Garden Security System ===")
    tulip = SecurePlant("Tulip", -8, -18)
    tulip.set_age(-8)
    tulip.set_height(18)
    tulip.get_info()


if __name__ == "__main__":
    main()
