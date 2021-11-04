#!/usr/bin/env python3

import json

path = "C:\dev\gloss.json"

with open(path, newline='') as f:
    text = f.read()

# Printing the raw text found in JSON file
# print(json_content)

data_json_dict = json.loads(text)

for key in data_json_dict:
    print(data_json_dict[key])



