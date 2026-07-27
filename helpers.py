import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2, backoff=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException:
            attempt += 1
            if attempt == retries:
                raise NetworkError(f'Failed to fetch {url} after {retries} attempts')
            time.sleep(delay)
            delay *= backoff
