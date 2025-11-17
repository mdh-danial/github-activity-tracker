# Github Activity Tracker
#### Project URL: https://roadmap.sh/projects/github-user-activity
## Description
A CLI project that tracks recent activity of a github user. Must include username in command line.


## Usage
```bash
git clone https://github.com/mdh-danial/github-activity-tracker.git
cd activity_tracker
python main.py <github username>
```

## Learning points
1. I learnt that REST API is a way for a client(me) to request data over the internet by sending a http request to a server and receiving requested data in the form of JSON 

2. Python uses requests library to make API call

3. steps to call REST API in python:
    1. Define API endpoint (URL)
    2. Send a GET request to the API 
    3. check if request is successful 
        - status code 200 = success
        - status code 304 = not modified
        - status code 403 = Forbidden
        - status code 503 = service unavailable

    4. convert response from JSON to python dictionary 

4. error messages starting with 4xx usually is client error while error messages starting with 5xx usually is server error

5. json.dumps helps to make data more readable with line breaks, indentation and proper formatting

6. Github public /events endpoint only shows event. You must specifically call the dictionary key you are looking for within each event to see for example, commits.