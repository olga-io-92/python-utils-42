def process_data(data):
    return [item for item in data if item is not None]


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_unique_items(items):
    return list(set(items))


def sort_items(items):
    return sorted(items)


def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]