#map
numbers = [1, 2, 3, 4, 5]

doubled = map(lambda x: x * 2, numbers)
print(list(doubled))

#filter
numbers = [1, 2, 3, 4, 5]

evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))

#reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, numbers)
print(sum)