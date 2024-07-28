# Decorators
- A decorator is a function that takes another function and extends its behavior without explicitly modifying it.

## Timing Decorator

- The `timing_decorator` function in this example measures the time it takes for a function to execute.

### Example
```py
from time import time
from functools import cache

def timing_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time()  # Record the end time

        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result  # Return the result of the function
    return wrapper

@timing_decorator
@cache
def sum(n):
    total = 1
    for i in range(1, n + 1):
        total += i
    return total

# Call the decorated function
result = sum(10_00_00_000)
print(result)

result = sum(10_00_00_000)
print(result)
```
### Output:
```
Function sum took 2.2739 seconds to execute
5000000050000001
Function sum took 0.0000 seconds to execute
5000000050000001
```
### We are using cache decorator to load the value of 1st sum of 10_00_00_000 into cache, so that when again we want the value it doesnt take time to calculate

- Once try to execute the code with out using the cache decorator
  