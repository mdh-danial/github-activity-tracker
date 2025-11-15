import requests
import sys

# obtain username from cli
if len(sys.argv) < 2:
    sys.exit("Usage: python main.py <github_username>")
else:
    username = sys.argv[1] 

