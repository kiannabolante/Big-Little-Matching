import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import OrderedDict
import pprint

scope = ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

little_sheet = client.open('Test CSE Little Sign Up (Autumn 2020) (Responses)').sheet1
big_sheet = client.open('Test Big Sign Up (Autumn 2020) (Responses)').sheet1
matches = client.open('Testing Matches').sheet1

littles = little_sheet.get_all_values()
bigs = big_sheet.get_all_values()

d = {}

mapping = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

class_standings = ["Freshman", "Sophomore", "Junior", "Senior", "Other"]

# for each little
#   add them to the mapping
#   for each big
#       if big's classes > little's classes
#           add them to the mapping's value
for little in littles[1:len(littles)]:
    key = little[7]
    mapping[key] = []
    for big in bigs[1:len(bigs)]:
        # comparing class standing
        if ((class_standings.index(big[8]) - class_standings.index(little[8])) > 0):
            # comparing classes
            if (len(big[12]) > len(little[12])):
                mapping[key].append(big[7])
    print(little[8])
    print(mapping[key])
    print()
        
    


