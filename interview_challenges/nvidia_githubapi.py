"""


APIs
Parse the response body and look for messages in each commit, and group by them for the count.
website URL: https://api.github.com/events

Please add the exception handler














answer)


try : 
    r = requests.get('https://api.github.com/events').text
    
    for event in r:
        commits = event.get('payload',{}).get('commits',[])
        for commit in commits:
            msg = commit.get("message")
            if not msg:
                continue
            result[msg] = result.get(msg,0)+1

    print(result)
except Exception as e:
    print(f"some exception: {e}")
"""

import json

with open("events.json") as jsonfile:
    json_content = jsonfile.read()
    
#above readline reads the file as a string, below we process that to a dict
events = json.loads(json_content)

for idx, e in enumerate(events):
    if e['type'] == 'PushEvent':
        print(idx, e['payload']['commits'][0]['message'], '\n\n')
