import csv
""" Generator uses yield keyword to retrieve the data instead, of looping 
through the list. using next() we can retrieve the next object.
reader = csv_reader('employee.csv') """

def csv_reader(filepath):
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            yield row
        

filepath = 'employee.csv'
csv_reader(filepath)
