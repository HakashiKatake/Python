n = int(input("Enter a number: "))
squares_dict = {x: x ** 2 for x in range(1, n + 1)}
print(f"Dictionary of squares from 1 to {n}: {squares_dict}")
