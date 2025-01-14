def string_length(s):
    count = 0
    for i in s:
        count += 1
    return count
s = input("Enter a string: ")
print(f"Length: {string_length(s)}")

