import json

#example 1
# file = open("interface.txt")
# contents = file.read()
# print(contents)
#
# file.close()


#example 2 with context manager
with open ("interface.txt") as f:
    myjson=f.read()


# with open ("interface.txt") as f:
#     myjson = json.loads(f.read())


