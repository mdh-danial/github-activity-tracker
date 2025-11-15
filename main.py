import requests
import sys

# obtain username from cli
if len(sys.argv) < 2:
    sys.exit("Usage: python main.py <github_username>")
else:
    username = sys.argv[1] 

# 1. Define API endpoint (URL)
# Example: https://api.github.com/users/<user>/events
url = f"https://api.github.com/users/{username}/events"

# 2. Send a GET request to the API
response = requests.get(url)

# check response status code
if response.status_code == 200:
    data = response.json()
    print("Data received:", data)

elif 400 <= response.status_code < 500:
    print(f"Client error ({response.status_code}): {response.text}")

elif 500 <= response.status_code < 600:
    print(f"Server error ({response.status_code}): {response.text}")

else:
    print(f"Unexpected status code: {response.status_code}")
