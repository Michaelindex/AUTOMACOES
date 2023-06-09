import json
import requests
import time

start_time = time.time()

while time.time() - start_time < 60:
    # Set the API endpoint
    url = "#"

    # Set the request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer #"
    }

    # Set the request data
    data = {
        "leaderId": "#",
        "playerId": "#",
        "playerType": "solo",
        "userIds" : ["#"],
        "0" : "#"

    }

    # Convert the data to json format
    payload = json.dumps(data)

    # Make the request
    response = requests.post('#', headers=headers, data=payload)

    # Print the response status code
    print(response.status_code)

    # Print the response content
    print(response.json())

    time.sleep(0.1)
