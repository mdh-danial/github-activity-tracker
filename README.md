# Github Activity Tracker

## Description

## Usage

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