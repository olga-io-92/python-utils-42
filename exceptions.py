import time

class RetryException(Exception):
    pass

def retry_request(func, max_attempts=3, delay=2):
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt < max_attempts - 1:
                time.sleep(delay)
            else:
                raise RetryException('Max retries exceeded') from e