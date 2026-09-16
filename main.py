import requests

import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200 if it worked
print(response.json())       # the response data

def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(2, 3))
