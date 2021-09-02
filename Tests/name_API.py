import requests


# source: https://juliensalinas.com/en/REST_API_fetching_go_golang_vs_python/
url = (
    "http://rc50-api.nameapi.org/rest/v5.0/parser/personnameparser?"
    "apiKey=4c812bf642f08aac955574296fd2d2d6-user1"
)

# Dict of data to be sent to NameAPI.org:
payload = {
    "inputPerson": {
        "type": "NaturalInputPerson",
        "personName": {
            "nameFields": [
                {
                    "string": "Pauwel",
                    "fieldType": "GIVENNAME"
                }, {
                    "string": "De Wilde",
                    "fieldType": "SURNAME"
                }
            ]
        },
        "gender": "UNKNOWN"
    }
}

# Proceed, only if no error:
try:
    # Send request to NameAPI.org by doing the following:
    # - make a POST HTTP request
    # - encode the Python payload dict to JSON
    # - pass the JSON to request body
    # - set header's 'Content-Type' to 'application/json' instead of
    #   default 'multipart/form-data'
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    # Decode JSON response into a Python dict:
    resp_dict = resp.json()
    print(resp_dict)
except requests.exceptions.HTTPError as e:
    print("Bad HTTP status code:", e)
except requests.exceptions.RequestException as e:
    print("Network error:", e)