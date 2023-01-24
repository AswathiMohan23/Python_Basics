# json.load() takes a file object and returns the json object.
# It is used to read JSON encoded data from a file and convert it into a Python dictionary
# and deserialize a file itself i.e. it accepts a file object.

import json

data = {
    "student": "Anna",
    "place": "Kochi",
    "skills": [
        "Drawing",
        "Singing",
        "dancing"
    ],

}
with open("read_json_data", "w") as write:
    json.dump(data, write)