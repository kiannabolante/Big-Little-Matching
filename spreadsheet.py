import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import OrderedDict
import pprint

# functions used for adding points when attribute had multiple options
def matching(littles, bigs, point):
    points = 0
    for little in littles:
        for big in bigs:
            if (little.lower() == big.lower()):
                points += point
    return points

scope = ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# opens the sheets 
# make sure you create the "matching" sheet as well
# make sure all of these documents have the project ID shared with them as well
little_sheet = client.open('Test CSE Little Sign Up (Spring 2021) (Responses)').sheet1
big_sheet = client.open('Test CSE Big Sign Up (Spring 2021) (Responses)').sheet1
matches = client.open('Testing Matches (Spring 2021)')

littles = little_sheet.get_all_values()
bigs = big_sheet.get_all_values()

# map to store all bigs who didn't get matched with anyone
bigs_left = {""}


# add all bigs to bigs-left set
for big in bigs[1:len(bigs)]:
    bigs_left.add(big[7])

bigs_left.discard("")

d = {}

mapping = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

class_standings = ["Freshman", "Sophomore", "Junior", "Senior", "Other", "BS/MS"]

worksheet = matches.get_worksheet(0)

row = 1 

# matching each little 
cell_list = []
for little in littles[1:len(littles)]:
    key = little[7]
    mapping[key] = []
    little_background = little[13].split(", ")
    little_living = little[14].split(", ")
    little_race = little[17].split(", ")
    little_interests = little[19].split(", ")
    little_hobbies = little[20].split(", ")
    little_activities = little[21].split(", ")
    little_ent = little[22].split(", ")
    little_food = little[23].split(", ")
    row += 1
    col = 1
    big_list = []
    for big in bigs[1:len(bigs)]:
        # comparing class standing
        points = 0
        if ((class_standings.index(big[8]) - class_standings.index(little[8])) > 0):    # might have to change this
            # comparing number of classes taken
            if (len(big[12]) > len(little[12])):
                big_background = big[13].split(", ")
                big_living = big[14].split(", ")
                big_race = big[17].split(", ")
                big_interests = big[19].split(", ")
                big_hobbies = big[20].split(", ")
                big_activities = big[21].split(", ")
                big_ent = big[22].split(", ")
                big_food = big[23].split(", ") 

                # compare timezone
                if (big[9] == little[9]):
                    points += 3
                    
                # match identities
                points += matching(little_background, big_background, 4)
                    
                # match living situation
                points += matching(little_living, big_living, 2)
                    
                # match sexuality
                if (big[16].lower() == little[16].lower()):
                    points += 4
                    
                # match race
                points += matching(little_race, big_race, 4)
                    
                # match technical interests
                points += matching(little_interests, big_interests, 1)

                # match hobbies
                points += matching(little_hobbies, big_hobbies, 2)

                # match activities
                points += matching(little_activities, big_activities, 2)

                # match entertainment
                points += matching(little_ent, big_ent, 1)

                # match food
                points += matching(little_food, big_food, 1)
                    
                # add big to map
                big_list.append([points, big[7]])

    # sorts bigs based on the number of points they have
    sorted_list = sorted(big_list, key=lambda x: x[0], reverse=True)  
    for big in sorted_list:
        mapping[key].append(big[0]) # points
        mapping[key].append(big[1]) # cse email
    values = mapping[key]
    values = [key] + values
    
    # google sheets goes from A-Z
    if (len(values) > 26):
        values = values[0:25]
    
    # discard big from bigs left
    for big in values:
        bigs_left.discard(big)
        
    end_col = chr(ord('A') + len(values) - 1)
    col_range = 'A' + str(row) + ':' + end_col + str(row)
    if (len(values) == 0):
        col_range = 'A' + str(row)
    curr_val = {'range': col_range, 'values': [values]}
    cell_list.append(curr_val)

# adding to spreadsheet
worksheet.batch_update(cell_list)

# prints the bigs who didn't get matched
print(bigs_left)

