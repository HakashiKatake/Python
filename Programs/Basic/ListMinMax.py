
numbers = list(map(int, input("Enter numbers: ").split()))
min = max = numbers[0]
for number in numbers:
    if number < min:
        min = number
    if number > max:
        max = number
print(f"List: {numbers}, Min: {min}, Max: {max}")
