import requests
import json

token = ''
name = ''


def headers(token):

    return {'Content-type': 'application/json',
            'Authorization': 'Bearer ' + token}

def webex_api(noun):

    return ''.join(('https://webexapis.com/v1/', noun))

def webex_get_me(name):
    uri = webex_api(name)
    return uri

uri = webex_get_me('people/me')
r = requests.get(uri, headers=headers(token))

# dir(r)
#
# mydetails = json.loads(r.text)
# type(mydetails)
# mydetails['id']
# mydetails['emails'][0]
