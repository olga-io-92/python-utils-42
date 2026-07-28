import time
import functools
import requests

class RetryExceededError(Exception):
    pass

def retry(max_retries=3, delay=1, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException:
                    retries += 1
                    if retries == max_retries:
                        raise RetryExceededError(f'Max retries exceeded for {func.__name__}')
                    time.sleep(delay)
                    delay *= backoff
        return wrapper
    return decorator

@retry(max_retries=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
