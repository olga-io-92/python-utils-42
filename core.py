import time
from functools import lru_cache

@lru_cache(maxsize=1024)
def expensive_computation(x):
    time.sleep(2)  # Simulating a long computation
    return x * x

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        results = []
        for item in self.data:
            results.append(expensive_computation(item))
        return results

if __name__ == '__main__':
    processor = DataProcessor(range(10))
    print(processor.process())