
lst = list(map(int, input("Enter numbers: ").split()))
first, second = float('-inf'), float('-inf')
for num in lst:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print(f"Second largest element: {second}")