#!/usr/bin/env python3

import json
import sys

jsonfile_loc = "nv-vk64.json"
samplefile_loc = "sample.txt"
#file = os.open(jsonfile_loc)

with open(jsonfile_loc, newline='') as jsonfile:
    json_content = jsonfile.read()

print(json_content)

jsoncontent = json.loads(json_content)

#print(type(jsoncontent))

for key in jsoncontent:
    print(jsoncontent[key])



