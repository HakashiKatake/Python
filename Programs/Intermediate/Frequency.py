
lst = list(map(int, input("Enter numbers: ").split()))
frequency = {}
for item in lst:
    frequency[item] = frequency.get(item, 0) + 1
print(f"Frequency of elements: {frequency}")