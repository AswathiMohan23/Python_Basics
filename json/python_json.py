# dumps() convert python object to json string
# dump() method is used for writing into json file

import json

dict = {
    "id":1,
    "name":"Tom",
    "class":"10th"
}
json_object = json.dumps(dict,indent =4)
print(json_object)