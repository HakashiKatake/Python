#Write a recursive function that computes the sum of all elements in a list.

def sumOfList(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sumOfList(lst[1:])
    
print(sumOfList([1, 2, 3, 4, 5])) # 15