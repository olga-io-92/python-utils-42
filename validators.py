import re

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_phone(phone):
    phone_regex = r'^\+?1?\d{9,15}$'
    return re.match(phone_regex, phone) is not None


def validate_url(url):
    url_regex = r'^(https?://)?(www\.)?[-a-zA-Z0-9@:%_\+.~#?&//=]+\.[a-zA-Z]{2,}(/\S*)?$'
    return re.match(url_regex, url) is not None


def validate_required_fields(data, required_fields):
    return all(field in data and data[field] for field in required_fields


if __name__ == '__main__':
    print(validate_email('test@example.com'))  # True
    print(validate_phone('+1234567890'))      # True
    print(validate_url('http://example.com'))  # True