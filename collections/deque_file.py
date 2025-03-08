from collections import deque
import csv
import os

def get_last_column(filename, column_name, n=5):
    """
    Return the last n values from the specified column in the CSV file
    """
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            column_values = deque((row[column_name] for row in reader), n)
        return column_values
    except OSError as e:
        print(f"An error occurred: {e}")
        raise
    except KeyError as e:
        print(f"Column not found: {e}")
        raise

result = get_last_column(r'C:\Users\shiri\Downloads\Work\Python_Project\PythonBasics\generator\employee.csv', 'email')
print(result)