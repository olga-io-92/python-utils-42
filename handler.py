import time
import requests
from requests.exceptions import RequestException

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException:
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            raise

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except Exception as e:
        print(f'Request failed: {e}')