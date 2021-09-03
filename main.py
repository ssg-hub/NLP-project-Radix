from Tests.name_API import To_Json, APIReq

givenName = "Curriculum"
surName = "Vitae"

try:
    rqst = To_Json(givenName, surName)
    name = APIReq(rqst)
    print(name)
except:
    pass