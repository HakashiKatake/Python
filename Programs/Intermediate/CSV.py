ilename = input("Enter the CSV filename: ")
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))