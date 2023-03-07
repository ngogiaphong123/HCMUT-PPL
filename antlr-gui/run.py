from functools import reduce

lst = [1, 2, 3, 4, 5]

result = reduce(lambda x, y, i: x + y + i, lst, 0)
print(result) # Output: 25