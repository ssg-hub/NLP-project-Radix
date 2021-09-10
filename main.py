from Tests.name_API import To_Json, APIReq
from Shilpa.tokens_for_name_extraction import tokensNameExtr

def get_name(pdf):

    realName = []
    # get first few tokens from pdf
    potNames = tokensNameExtr(pdf)
    print(potNames)

    # zip the tuples per pair as follows: (1, 2), (2, 3), (3, 4), etc.
    for item in potNames:
        perPair = zip(potNames, potNames[1:])

    # store the zip in a list
    # assign the different parts to potential given name and surname
    # run the suggestions through the API
    perPair = list(perPair)
    for index, pair in enumerate(perPair):
        givenName = pair[0]
        surName = pair[1]

        if givenName.lower() not in ["curriculum", "vitae"]:
            if surName.lower() not in ["curriculum", "vitae"]:
                try:
                    rqst = To_Json(givenName, surName)
                    name = APIReq(rqst)
                    realName.append(name)
                except:
                    pass
        
    return realName[0]

print(get_name("/home/becode/Documents/GitHub/NLP-project-Radix/assets/pdfs/1478.pdf"))