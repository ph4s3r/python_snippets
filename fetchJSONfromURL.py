import urllib.request
import urllib.parse
"""
# method 1: just a simple get
with urllib.request.urlopen("http://api.github.com/events") as response:
    events = response.read()
"""

"""
#there is a request object separately
req = urllib.request.Request("http://api.github.com/events")

with urllib.request.urlopen(req) as resp:
    events = resp.read()

"""

"""
#POST request with some data provided in tuples
url = "http://api.github.com/events"

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }

headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)

req = urllib.request.Request(url, data, headers)
"""


url = "https://api.github.com/events"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as resp:
    events = resp.read()



