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
        "Authorization": "Bearer 64193c63-1f06-4dc7-b36d-99061618029b"
    }

    # Set the request data
    data = {
        "leaderId": "ee4d0675-d8db-43ea-8137-390f4a9277d0",
        "playerId": "ee4d0675-d8db-43ea-8137-390f4a9277d0",
        "playerType": "solo",
        "userIds" : ["ee4d0675-d8db-43ea-8137-390f4a9277d0"],
        "0" : "ee4d0675-d8db-43ea-8137-390f4a9277d0"

    }

    # Convert the data to json format
    payload = json.dumps(data)

    # Make the request
    response = requests.post('https://api.faceit.com/queue/v2/player', headers=headers, data=payload)

    # Print the response status code
    print(response.status_code)

    # Print the response content
    print(response.json())

    time.sleep(0.1)
