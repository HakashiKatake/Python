numbers = list(map(int, input("Enter numbers: ").split()))
left, right = 0, len(numbers) - 1
while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1
print(f"Reversed List: {numbers}")