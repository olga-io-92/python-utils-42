import time
import functools


def performance_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Performance: {func.__name__} executed in {end_time - start_time:.4f}s')
        return result
    return wrapper


@performance_timer
def heavy_computation(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total


@performance_timer
def data_processing(data):
    return [item * 2 for item in data]


if __name__ == '__main__':
    print(heavy_computation(100000))
    print(data_processing([1, 2, 3, 4, 5]))