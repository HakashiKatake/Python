

import csv

def readCSV(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
           

readCSV('Python/Programs/Advanced/CSVC.csv')