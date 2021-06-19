# Author: Brandon Hoffman
# Date: 10/24/2020
# Description: Create a taxicab class that tracks changes to x and y coordinates and total odometer changes


class Taxicab:
    """
    Represents a taxicab that tracks the distance traveled when given x and y coordinates
    """
    def __init__(self, x, y):
        """
        Creates a taxicab object with x and y coordiantes and intializes an odometer to 0
        """
        self._x = x
        self._y = y

        self._odometer = 0

    def get_x_coord(self):
        """
        returns the current x coordinate
        """
        return self._x

    def get_y_coord(self):
        """
        returns the current y coordinate
        """
        return self._y

    def get_odometer(self):
        """
        sums the abs value of the change in x and y coordinates
        """
        return self._odometer

    def move_x(self, x_vector):
        """
        takes in a one-dimensional vector and adds it to the x coordiante as its original value and the odometer as an absolute value
        """
        self._x += x_vector
        self._odometer += abs(x_vector)

    def move_y(self, y_vector):
        """
        takes in a one-dimensional vector and adds it to the x coordiante as its original value and the odometer as an absolute value
        """
        self._y += y_vector
        self._odometer += abs(y_vector)




