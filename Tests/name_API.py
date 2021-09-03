import requests
from requests.exceptions import HTTPError

# source: https://juliensalinas.com/en/REST_API_fetching_go_golang_vs_python/
url = (
    "http://rc50-api.nameapi.org/rest/v5.0/parser/personnameparser?"
    "apiKey=4c812bf642f08aac955574296fd2d2d6-user1"
)

# Dict of data to be sent to NameAPI.org:
def To_Json(givenname: str, surname: str):
    payload = {
        "inputPerson": {
            "type": "NaturalInputPerson",
            "personName": {
                "nameFields": [
                    {
                        "string": givenname,
                        "fieldType": "GIVENNAME"
                    }, {
                        "string": surname,
                        "fieldType": "SURNAME"
                    }
                ]
            },
            "gender": "UNKNOWN"
        }
    }
    return payload

# Proceed, only if no error:
def APIReq(rqst: dict):
    # Send request to NameAPI.org by doing the following:
    # - make a POST HTTP request
    # - encode the Python payload dict to JSON
    # - pass the JSON to request body
    # - set header's 'Content-Type' to 'application/json' instead of
    #   default 'multipart/form-data'
    resp = requests.post(url, json = rqst)
    resp.raise_for_status()
    # Decode JSON response into a Python dict:
    resp_dict = resp.json()

    # Check the confidence scores
    step = resp_dict["matches"]
    values = [i["confidence"] for i in step if "confidence" in i]
    print(values)
    # Print name if confidence score for at least one part of name > 0.5
    if values[0] or values[1] > 0.5:
        step2 = step[0]
        return step2["parsedPerson"]["addressingGivenName"], step2["parsedPerson"]["addressingSurname"]
