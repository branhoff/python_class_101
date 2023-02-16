# Author: Brandon Hoffman
# Date: 10/17/2020
# Description: created a function called "fall_distance() that takes an input of seconds and returns
#              the distance an object has fallen."

time: int = int(input("Please enter an amount of time in second(s): "))


def fall_distance(t:int) -> float:
    """takes input in seconds and returns distance object has fallen"""
    g: float = 9.8  # velocity

    return 0.5 * g * t * t


print("The distance the object has fallen is : ", fall_distance(time), "meter:")
