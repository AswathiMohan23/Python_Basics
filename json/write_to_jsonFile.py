# dump() mehod is used to write to json file

import json

dict = {
    "id":1,
    "name":"Harry",
    "class":"8th"
}
with open("data.json","w") as outfile:
    json.dump(dict,outfile)

# here if data.json file is not present then it creates one and write data into that file