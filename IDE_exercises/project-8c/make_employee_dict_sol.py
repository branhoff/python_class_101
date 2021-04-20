# Author: Brandon Hoffman
# Date: 11/14/2020
# Description: Creates an Employee object to store common charactersitcs of an employee
#              Creates a function, make_employees_dict that takes a list of these characteristics and
#              returns a dictionary where the key is the id numbers and the value is the Employee object

class Employee:
    """
    Represents fundamental characteristics of an employee of a company
    """

    def __init__(self, name, ID_number, salary, email_address):
        """
        Creates an Employeee object with name, ID_number, salary, and email_address values
        """
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """
        returns employee name
        """
        return self._name
    
    def get_ID_number(self):
        """
        returns employee ID number
        """
        return self._ID_number

    def get_salary(self):
        """
        returns employee salary
        """
        return self._salary

    def get_email_address(self):
        """
        returns employee email_address
        """
        return self._email_address

def make_employee_dict(names, id_nums, salaries, email_addresses):
    """
    Input: 4 lists of names, id numbers, salaries, and email_addresses of equal length
    Output: a dictionary where the id num is the key and the Employee object the value
    """

    employee_dict = {}

    i = 0
    for id_ in id_nums:
        employee_dict[id_] = Employee(names[i], id_nums[i], salaries[i], email_addresses[i])
        i += 1

    return employee_dict