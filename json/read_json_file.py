import json
# read json file

with open("read_file.json", "r") as read_content:
    print(json.load(read_content))