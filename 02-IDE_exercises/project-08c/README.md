# project-08c

Write a Python class called Employee that has **private** variables for an employee's name, ID_number, salary, and email_address. The class should have an init class to initialize the object and getter methods for each data variables. 

Write a separate Python function (separate from the Employee class) called **make_employee_dict** that takes in a  list of names, 
a list of ID numbers, a list of salaries and a list of email addresses (which are all the same length) as parameters.  
The function should iterate through each list to create Employee objects and add these objects to the dictionary where the key is the ID number and the value for that key is the whole Employee object.  
The function should return the resulting dictionary.

For example, it could be used like this:
```
emp_names = ["Tuan", "Rachel", "Brandon"]
emp_ids = ["1000", "1001", "1002"]
emp_sals = [30, 35, 28]
emp_emails = ["Tuan@aol.com", "Rachel@aol.com", "Brandon@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
print(result["100"].get_name())
```

Remember in your testing that printing an object of a user-defined class will just print out the object's type and address in memory.  If you want to print the values of its data members, you need to call its get functions, as shown in the print statement above.

The file should be named: make_employee_dict.py
