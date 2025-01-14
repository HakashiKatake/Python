s = input("Enter a string to convert to integer: ")
try:
    num = int(s)
    print(f"Converted number: {num}")
except ValueError:
    print("Conversion error: Not a valid integer")