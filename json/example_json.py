import json

data_dict =""" {
    "name": "Harry",
    "id": 68,
    "age": 15,
    "class": "10th",
    "school": "abc school"}"""

dict_to_json = json.dumps(data_dict)
print(dict_to_json)
