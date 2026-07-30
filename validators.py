def validate_email(email: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None


def validate_username(username: str) -> bool:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,29}$'
    return re.match(pattern, username) is not None


def validate_password(password: str) -> bool:
    return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)