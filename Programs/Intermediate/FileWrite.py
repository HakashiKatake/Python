filename = input("Enter the filename to write: ")
content = input("Enter the content: ")
with open(filename, 'w') as file:
    file.write(content)