import config

import json
from requests import get

def getState(entity):
    headers = {
        "Authorization": "Bearer {key}".format(key = config.HOME_ASSISTANT_KEY),
        "content-type": "application/json",
    }

    endpoint = "{url}/api/states/{entity}".format(url = config.HOME_ASSISTANT_URL, entity = entity)

    response = get(endpoint, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data["state"]
        
def getColor(entity):
    headers = {
        "Authorization": "Bearer {key}".format(key = config.HOME_ASSISTANT_KEY),
        "content-type": "application/json",
    }

    endpoint = "{url}/api/states/{entity}".format(url = config.HOME_ASSISTANT_URL, entity = entity)

    response = get(endpoint, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        if "rgb_color" in data["attributes"]:
            return data["attributes"]["rgb_color"]
        else:
            return (0, 0, 0)