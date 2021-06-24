# project-05b


Write a Python class called Taxicab that has three **private** instance variables: 
one variable for x-coordinate, y-coordinate, 
and odometer reading of the Taxicab.  
The class should have an init method that takes two parameters and uses them to initialize the coordinates, and  the  odometer to  zero 
The class should have getter methods for each variable for each data member: get_x_coord, get_y_coord, and get_odometer.  
The class should have a method called move_x that takes a parameter that tells how far the Taxicab should shift left or right and move_y to tell how  far the  Taxicab shift up or down
For example, the Taxicab class might be used as follows:
```
cab = Taxicab(3, -8)       # creates a Taxicab object at coordinates (3, -8)
cab.move_x(4)              # moves cab 4 units "right"
cab.move_y(-5)             # moves cab 5 units "down"
cab.move_x(-2)             # moves cab 2 unit "left"
print(cab.get_odometer())  # prints the current odometer reading
```

The file should be named: Taxicab.py