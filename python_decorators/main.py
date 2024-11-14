from collections.abc import Callable
from typing import Any

import time
import requests
from functools import wraps



def square(func: Callable):
    def wrapper(a: Any, b: Any):
        return func(a,b)**2

    return wrapper

@square
def func1(a: Any, b:Any) -> Any:
    return a+b


def retry(num_retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(num_retries):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < num_retries - 1:
                        time.sleep(delay)
                    else:
                        print("All retry attempts failed.")
                        raise
        return wrapper
    return decorator

@retry(num_retries=5, delay=3)
def make_request(url):
    response = requests.get(url)
    response.raise_for_status()  
    return response


if __name__ == "__main__":
    print(func1(3,4))

    try:
        response = make_request("https://example.com")
        print(response.text)
    except requests.RequestException:
        print("Request failed after retries.")
