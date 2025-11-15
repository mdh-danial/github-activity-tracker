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

# 3. Check for successful request (status code 200)
if response.status_code == 200:
    # 4. convert response frpm JSON to Python dict
    data = response.json()
    print("Data received", data)

elif response.status_code == 404:
    print("username not found, ERROR:  ", response.status_code)
