string = '{"pets": ["cat", "dog"]}'
type(string)


import json
data = json.loads(string)
type(data)

# data["pets"][1]
