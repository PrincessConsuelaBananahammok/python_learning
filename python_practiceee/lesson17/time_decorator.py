import random
import time

import requests


#декоратор що буде рахувати скільки часу виконувалась функція
def time_checker(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"It takes {end_time - start_time} to execute the function")
        return result

    return wrapper

@time_checker
def send_requests_to_db():
    print("sending requests")
    time.sleep(random.choice(range(5)))

for _ in range (5):
    send_requests_to_db()
