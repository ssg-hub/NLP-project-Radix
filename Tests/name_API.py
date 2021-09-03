import requests
import jsonpickle


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
    print(type(payload))
    return payload

rqst = jsonpickle.encode(To_Json(givenname = "John", surname = "Doe"))
print(rqst)

# Proceed, only if no error:
try:
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
    print(resp_dict)
    # Select the confidence scores
    step = resp_dict["matches"]
    values = [i["confidence"] for i in step if "confidence" in i]
    print(values)

except requests.exceptions.HTTPError as e:
    print("Bad HTTP status code:", e)
except requests.exceptions.RequestException as e:
    print("Network error:", e)

    