filename = input("Enter the JSON filename: ")
key = input("Enter the key to modify: ")
value = input("Enter the new value: ")
with open(filename, 'r') as file:
    data = json.load(file)
data[key] = value
with open(filename, 'w') as file:
    json.dump(data, file, indent=4)