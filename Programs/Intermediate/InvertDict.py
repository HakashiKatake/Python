d = dict(input("Enter key value pairs: ").split() for _ in range(int(input("Enter number of pairs: "))))
inverted_dict = {v: k for k, v in d.items()}
print(f"Inverted dictionary: {inverted_dict}")