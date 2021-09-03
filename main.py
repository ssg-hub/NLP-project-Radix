from Tests.name_API import To_Json, APIReq



givenName = "BERT"
surName = "Herreweghe"

try:
    rqst = To_Json(givenName, surName)
    name = APIReq(rqst)
    print(name)
except:
    pass