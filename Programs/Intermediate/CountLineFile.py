filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    line_count = 0
    for i in file:
        line_count += 1
    print(f"Number of lines: {line_count}")