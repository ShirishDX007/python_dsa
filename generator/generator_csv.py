import csv
""" Generator uses yield keyword to retrieve the data instead, of looping 
through the list. using next() we can retrieve the next object.
reader = csv_reader('employee.csv') 
next(reader) to retrieve the next object."""

def csv_reader(filepath):
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            yield row
       
if __name__ == '__main__':
    filepath = 'employee.csv'
    for row in csv_reader(filepath):
        print(row)
