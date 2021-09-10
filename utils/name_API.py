import requests
from tokens_for_name_extraction import tokensNameExtr

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
    # source: https://juliensalinas.com/en/REST_API_fetching_go_golang_vs_python/
    # Send request to NameAPI.org by doing the following:
    # - make a POST HTTP request
    # - encode the Python payload dict to JSON
    # - pass the JSON to request body
    # - set header's 'Content-Type' to 'application/json' instead of
    #   default 'multipart/form-data'
    url = ("http://rc50-api.nameapi.org/rest/v5.0/parser/personnameparser?apiKey=4c812bf642f08aac955574296fd2d2d6-user1")
    resp = requests.post(url, json = rqst)
    resp.raise_for_status()
    # Decode JSON response into a Python dict:
    resp_dict = resp.json()

    # Check the confidence scores
    step = resp_dict["matches"]
    values = [i["confidence"] for i in step if "confidence" in i]
    # Return name if confidence score for at least one part of name > 0.7
    if values[0] or values[1] > 0.7:
        step2 = step[0]
        return step2["parsedPerson"]["addressingGivenName"] + " " + step2["parsedPerson"]["addressingSurname"]

def get_name(pdf):

    realName = []
    # get first few tokens from pdf
    potNames = tokensNameExtr(pdf)
    # print("potential names: ", potNames)

    # zip the tuples per pair as follows: (1, 2), (2, 3), (3, 4), etc.
    for item in potNames:
        perPair = zip(potNames, potNames[1:])

    # store the zip in a list
    # assign the different parts to potential given name and surname
    # run the suggestions through the API
    perPair = list(perPair)
    # print("per pair: ", perPair)
    for index, pair in enumerate(perPair):
        givenName = pair[0]
        surName = pair[1]

        if givenName.lower() not in ["curriculum", "vitae", "resume"]:
            if surName.lower() not in ["curriculum", "vitae", "resume"]:
                try:
                    rqst = To_Json(givenName, surName)
                    name = APIReq(rqst)
                    # print("names: ", name)
                    realName.append(name)
                except:
                    pass
        
    if len(realName) > 0:
        return realName[0]
    else:
        return ""

print(get_name("/home/becode/Documents/GitHub/NLP-project-Radix/assets/pdfs/345.pdf"))