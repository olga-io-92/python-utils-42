import re

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def validate_phone(phone):
    phone_regex = r'^(\+?\d{1,3}[- ]?)?\(?\d{1,4}\)?[- ]?\d{1,4}[- ]?\d{1,9}$'
    return re.match(phone_regex, phone) is not None


def validate_url(url):
    url_regex = r'^(https?://)?(www\.)?([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,6})([/\w .-]*)*/?$'
    return re.match(url_regex, url) is not None


def validate_postal_code(postal_code):
    postal_code_regex = r'^[A-Za-z]\d[A-Za-z] ?\d[A-Za-z]\d$'
    return re.match(postal_code_regex, postal_code) is not None