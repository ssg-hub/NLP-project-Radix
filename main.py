from Tests.name_API import To_Json, APIReq



givenName = "Harold"
surName = "Zuluaga duque"

try:
    rqst = To_Json(givenName, surName)
    name = APIReq(rqst)
    print(name)
except:
    pass