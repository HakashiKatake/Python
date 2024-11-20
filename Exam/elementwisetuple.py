#element wise tuple sum

tuples = [(1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1)]
result = tuple(map(sum, zip(*tuples)))
print("Element-wise sum:", result)