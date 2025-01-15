
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from functools import reduce
lst = list(filter(lambda x: x % 2 == 0, lst))
print(lst)
print(reduce(lambda x, y: x + y, lst)) 

