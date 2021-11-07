
"""

This module gets some json from an API endpoint and parses it

"""


import urllib.error
import urllib.request as r
import sys
import logging
import socket
import json


def fetcher(url: str):

    req = r.Request(url)
    socket.setdefaulttimeout(timeout)

    try:
        with r.urlopen(req) as response:
            data = response.read().decode()
            logging.debug(f"Data acquired. Response type: "
                          f"{type(data)} size: "
                          f"{sys.getsizeof(data)}")
            return data



    except urllib.error.HTTPError as e:
        logging.error(f"Got back a non-200 HTTP Status code: {e.reason}")
        exit(2)

    except urllib.error.URLError as e:
        logging.error(f"Unable to fetch URL. Reason: {e.reason}")
        exit(1)

def jsonParser(d):

    try:
        jsondata = json.loads(d)
        logging.debug(f"response successfully deserialized as JSON: {type(jsondata)}")
        return jsondata
    except:
        logging.error(f"response type of {type(data)} could not be deserialized as JSON, exiting")
        exit(1)

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)
    timeout = 10
    # data = fetcher('https://api.github.com/events')
    data = fetcher('https://jsonplaceholder.typicode.com/todos/2')
    json_data = jsonParser(data)
    print(type(json_data))
    for item in json_data: # github events is a list, iterating through
        pass





