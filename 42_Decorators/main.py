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