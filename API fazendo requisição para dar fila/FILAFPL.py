import json
import requests
import time

start_time = time.time()

while time.time() - start_time < 60:
    # Set the API endpoint
    url = "https://api.faceit.com/queue/v2/player"

    # Set the request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": ""
    }

    # Set the request data
    data = {
        "entityId" : "",
        "entityType" : "hub",
        "leaderId": "",
        "playerId": "",
        "playerType": "solo",
        "userIds" : [""],
        "0" : ""

    }

    # Convert the data to json format
    payload = json.dumps(data)

    # Make the request
    response = requests.post('https://api.faceit.com/queue/v2/player', headers=headers, data=payload)

    # Print the response status code
    print(response.status_code)

    # Print the response content
    print(response.json())
    
    if response.status_code == 200:
        break
    else:
        time.sleep(0.1)