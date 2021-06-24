# project-06c

Write a Python class called Person that has two private instance variables - the person's name and age. 

It should have an init method that takes two values and initialize them.  It should have a get_age method.

Write a separate Python function (separated from the Person class) called std_dev that takes as a parameter a list of Person objects and returns the standard deviation of all their ages

To calculate the standard deviation, you'll need to take a square root or exponent of 0.5. 

For example, the result of 9^(0.5) would be 3.0.  Python does have a specific sqrt() function, but that involves importing a module, which we haven't covered yet.

Here's a simple example of how your class and function could be used:
```
person1 = Person("Katie", 73)
person1 = Person("Tran", 24)
person1 = Person("Hanna", 48)
person_list = [person1, person1, person1]
answer = std_dev(person_list)
```

The file should be named: std_dev.py
