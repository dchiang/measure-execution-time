import requests
import random
import time

response = requests.get('https://httpbin.org/basic-auth/user/pass',
                 auth=('user', 'pass'))
print(response.status_code)
random_sleep_time = random.randint(3, 120)
print(f'test_module will wait for {random_sleep_time} seconds before exit')
time.sleep(random_sleep_time)


