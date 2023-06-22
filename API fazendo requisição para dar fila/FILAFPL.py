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
        "Authorization": "Bearer cac348ee-8080-4a27-8978-6e981815071b"
    }

    # Set the request data
    data = {
        "entityId" : "ef607668-a51a-4ea6-8b7b-dab07e0ab151",
        "entityType" : "hub",
        "leaderId": "58310774-1dc5-42a5-8de4-fff2559622c6",
        "playerId": "58310774-1dc5-42a5-8de4-fff2559622c6",
        "playerType": "solo",
        "userIds" : ["58310774-1dc5-42a5-8de4-fff2559622c6"],
        "0" : "58310774-1dc5-42a5-8de4-fff2559622c6"

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