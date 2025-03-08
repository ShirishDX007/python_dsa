from collections import namedtuple
import csv
import os

Parts = namedtuple('Parts', 'id desc cost amount')
auto_parts = Parts(id=11234, desc='Ford Engine', cost=1250.00, amount=100)
print(auto_parts.id)

#namedtuple is a factory function for creating tuple subclasses with named fields.
# namedtuple are useful for assigning field names to result tuples return by the csv or sqlite3 modules.

EmployeeRecord = namedtuple('EmployeeRecord', ['lastName', 'firstName','jobTitle'])

try:
    with open('employee.csv', 'r') as file:
        reader = csv.DictReader(file)
        next(reader)
        for row in reader:
            emp = EmployeeRecord(
                lastName=row['lastName'],
                firstName=row['firstName'],
                jobTitle=row['jobTitle']
            )
            print(emp.lastName,emp.firstName, emp.jobTitle)       
except FileNotFoundError:
    print("File not found")
