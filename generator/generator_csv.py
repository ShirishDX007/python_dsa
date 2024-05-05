import csv

def csv_reader(filepath):
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            yield row
        

filepath = 'employee.csv'
csv_reader(filepath)
