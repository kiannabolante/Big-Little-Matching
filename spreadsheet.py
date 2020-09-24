import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import OrderedDict
import pprint

scope = ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

little_sheet = client.open('Test CSE Little Sign Up (Autumn 2020) (Responses)').sheet1
big_sheet = client.open('Test Big Sign Up (Autumn 2020) (Responses)').sheet1
matches = client.open('Testing Matches')

littles = little_sheet.get_all_values()
bigs = big_sheet.get_all_values()

d = {}

mapping = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

class_standings = ["Freshman", "Sophomore", "Junior", "Senior", "Other"]

#worksheet = matches.sheet1
worksheet = client.open('Test Big Sign Up (Autumn 2020) (Responses)').get_worksheet(1)

row = 1 # update for each little

# matching
for little in littles[1:len(littles)]:
    key = little[7]
    mapping[key] = []
    little_background = little[13].split(", ")
    little_race = little[17].split(", ")
    little_interests = little[19].split(", ")
    little_living = little[14].split(", ")
    row += 1
    col = 1
    big_list = []
    for big in bigs[1:len(bigs)]:
        # comparing class standing
        points = 0
        if ((class_standings.index(big[8]) - class_standings.index(little[8])) > 0):    # might have to change this
            # comparing number of classes taken
            if (len(big[12]) > len(little[12])):
                # comparing hours
             #   if (big[10] == little[10]):
                    # match identities
                    big_living = big[14].split(", ")
                    big_background = big[13].split(", ")
                    big_race = big[17].split(", ")
                    big_interests = big[19].split(", ")
                    for little_back in little_background:
                        for big_back in big_background:
                            if (little_back == big_back):
                                points += 3
                    # match living situation
                    for lit_living in little_living:
                        for b_living in big_living:
                            if (lit_living == b_living):
                                points += 2
                    # match pronouns
                    if (big[15] == little[15]): # hesitant on adding these
                        points += 2
                    # match sexuality
                    if (big[16].lower() == little[16].lower()):
                        points += 2
                    # match race
                    for lit_race in little_race:
                        for b_race in big_race:
                            if (lit_race == b_race):
                                points += 2
                    # match interests
                    for little_int in little_interests:
                        for big_int in big_interests:
                            if (little_int == big_int):
                                points += 1
                    # add big to map
                    if (points >= 7):
                       # mapping[key].append(big[7])
                       big_list.append([points, big[7]])
    sorted_list = sorted(big_list, key=lambda x: x[0], reverse=True)  
    for big in sorted_list:
        mapping[key].append(big[0])
        mapping[key].append(big[1])
    # adding bigs to spreadsheet
    values = mapping[key]
    col = 'B'
    end_col = chr(ord('a') + len(values))
    col_range = col + str(row) + ':' + end_col.capitalize() + str(row)
    cell_list = worksheet.range(col_range)
    for i, val in enumerate(values):
        cell_list[i].value = val
    if (len(cell_list) > 0):
        worksheet.update_cells(cell_list)
    
# adding littles to spreadsheet
row = 2
for key in mapping:
    worksheet.update_cell(row, 1, key)
    row += 1





    


