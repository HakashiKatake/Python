filename = input("Enter the filename to read: ")
with open(filename, 'r') as file:
    print(file.read())