import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time of {func.__name__}: {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@timeit
def expensive_computation(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

@timeit
def optimized_computation(n):
    return sum(i ** 2 for i in range(n))

if __name__ == '__main__':
    print(expensive_computation(10000))
    print(optimized_computation(10000))