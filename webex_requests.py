import requests
import json

token = ''


def _headers(token):

    return {'Content-type': 'application/json',
            'Authorization': 'Bearer ' + token}

def _webex_api(noun):
    """
    returns the proper Spark URI based on the given noun
    In:
        noun: Spark noun (rooms, messages, ...), (str)
    Out:
        URL (str)
    """
    return ''.join(('https://webexapis.com/v1/', noun))

def webex_get_me(name):
    uri = _webex_api(name)
    return uri

uri = webex_get_me('people/me')
r = requests.get(uri, headers=_headers(token))

dir(r)

mydetails = json.loads(r.text)
type(mydetails)
mydetails['id']
mydetails['emails'][0]
