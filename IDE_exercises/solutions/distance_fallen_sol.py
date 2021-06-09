# Author: Brandon Hoffman
# Date: 10/17/2020
# Description: created a function called "fall_distance() that takes an input of seconds and returns
#              the distance an object has fallen."


def fall_distance(t):
    '''takes input in seconds and returns distance object has fallen'''
    g = 9.8 # velocity

    return 0.5 * g * t*t

