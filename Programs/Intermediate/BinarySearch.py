arr = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter the number to search for: "))
left, right = 0, len(arr) - 1
found = False
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
print(f"Element {'found' if found else 'not found'} at index {mid if found else -1}")