#!/usr/bin/env python3
def check_temperature(temp_str):
    """ Function that convert string to integer and check if the temperature
    is reasonable for plants"""
    try:
        tmp = int(temp_str)
        if tmp > 0 and tmp < 40:
            print(f"Temperature {tmp}°C is perfect for plants!")
        elif tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """ Function that checks that check_temperature handels all inputs"""
    values = ["12", "32", "110", "-8", "hii"]
    for v in values:
        print("Testing temperature :", v)
        check_temperature(v)
        print("")


print("=== Garden Temperature Checker ===")
print("")
test_temperature_input()
print("All tests completed - program didn't crash!")
