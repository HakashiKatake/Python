#Implement binary search recursively to find an element in a sorted list.

def binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            return binary_search(lst[mid+1:], target)
        
        else:
            return binary_search(lst[:mid], target)

print(binary_search([1, 2, 3, 4, 5], 3)) # True