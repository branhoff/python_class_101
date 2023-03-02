from Taxicab import Taxicab

cab = Taxicab(3, -8)       # creates a Taxicab object at coordinates (3, -8)
cab.move_x(4)              # moves cab 4 units "right"
cab.move_y(-5)             # moves cab 5 units "down"
cab.move_x(-2)             # moves cab 2 unit "left"
print(cab.get_odometer())  # prints the current odometer reading