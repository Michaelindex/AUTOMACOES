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
        "leaderId": "f4f8db79-0e8a-4a12-a2f0-fee9537219e7",
        "playerId": "f4f8db79-0e8a-4a12-a2f0-fee9537219e7",
        "playerType": "solo",
        "userIds" : ["f4f8db79-0e8a-4a12-a2f0-fee9537219e7"],
        "0" : "f4f8db79-0e8a-4a12-a2f0-fee9537219e7"

    }

    # Convert the data to json format
    payload = json.dumps(data)

    # Make the request
    response = requests.post('#', headers=headers, data=payload)

    # Print the response status code
    print(response.status_code)

    # Print the response content
    print(response.json())
    
    if response.status_code == 200:
        break
    else:
        time.sleep(0.1)