def clean_string(s):
    return ' '.join(s.split()).strip()


def is_empty(s):
    return not bool(s.strip())


def to_lowercase(s):
    return s.lower() if s else ''


def extract_numbers(s):
    return [int(num) for num in s.split() if num.isdigit()]


def flatten_list(lst):
    return [item for sublist in lst for item in sublist]


def generate_range(start, end):
    return list(range(start, end + 1))


def sort_dict_by_key(d):
    return dict(sorted(d.items()))


def reverse_string(s):
    return s[::-1]


def list_to_string(lst, separator=', '):
    return separator.join(lst)


def remove_duplicates(lst):
    return list(set(lst))