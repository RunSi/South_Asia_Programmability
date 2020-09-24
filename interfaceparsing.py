import json
from pprint import pprint

f = open('interface.txt')
jsonfile = f.read()

jsondict = json.loads(jsonfile)

