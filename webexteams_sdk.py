from webexteamssdk import WebexTeamsAPI

accesstoken = ''

api = WebexTeamsAPI(access_token=accesstoken)

mydetails = api.people.me()

#examples
#dir(api)
#help(api)
#mydetails.id
#mydetails.emails
#for x in api.rooms.list():
#    print(x)