numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter number to count: "))
count = 0
for number in numbers:
    if number == target:
        count += 1
print(f"Occurrences: {count}")