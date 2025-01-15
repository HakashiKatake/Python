
filename = input("Enter the filename: ")
find = input("Enter the string to find: ")
replace = input("Enter the string to replace: ")
with open(filename, 'r') as file:
    content = file.read()
content = content.replace(find, replace)
with open(filename, 'w') as file:
    file.write(content)
print("Replaced successfully")