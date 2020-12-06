# project-8c

Write a class named Employee that has **private** data members for an employee's name, ID_number, salary, and email_address.It should have an init method that takes four values and uses them to initialize the data members. It should have get methods named get_name, get_ID_number, get_salary, and get_email_address.

Write a separate function (not part of the Employee class) named **make_employee_dict** that takes as parameters a list of names, a list of ID numbers, a list of salaries and a list of email addresses (which are all the same length).  The function should take the first value of each list and use them to create an Employee object.  It should do the same with the second value of each list, etc. to the end of the lists.  As it creates these objects, it should add them to a dictionary, where the key is the ID number and the value for that key is the whole Employee object.  The function should return the resulting dictionary.

For example, it could be used like this:
```
emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
print(result["100"].get_name())
```

Remember in your testing that printing an object of a user-defined class will just print out the object's type and address in memory.  If you want to print the values of its data members, you need to call its get functions, as shown in the print statement above.

The file must be named: make_employee_dict.py
