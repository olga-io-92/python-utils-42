def is_palindrome(string):
    return string == string[::-1]


def factorial(n):
    if n < 0:
        raise ValueError('Negative values are not allowed.')
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n < 0:
        raise ValueError('Negative values are not allowed.')
    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)
    return sequence[:n]


def flatten(nested_list):
    flattened = []
    for sublist in nested_list:
        for item in sublist:
            flattened.append(item)
    return flattened


def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}