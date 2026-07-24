import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"{func.__name__} executed in {duration:.4f} seconds")
        return result
    return wrapper

@timeit
def example_expensive_function(data):
    total = 0
    for value in data:
        total += value ** 2
    return total

if __name__ == "__main__":
    data = range(10**6)
    print(example_expensive_function(data))
