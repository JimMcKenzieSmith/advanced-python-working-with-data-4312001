# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print("Total quakes:",len(data["features"]))
felt_by_100 = sum(q["properties"]["felt"] != None and q["properties"]["felt"] >= 100
                  for q in data["features"])
print(f"Total qualkes felt by at least 100 people: {felt_by_100}")

def get_felt(q):
    if q["properties"]["felt"] == None:
        return 0
    return int(q["properties"]["felt"])

data["features"].sort(key=get_felt, reverse=True)
most_mag = data["features"][0]["properties"]
print(f"Most felt reports: M {most_mag['mag']} - {most_mag['place']}, reports: {most_mag['felt']}")
def get_sig(q):
    return int(q["properties"]["sig"])

data["features"].sort(key=get_sig, reverse=True)
print("The 10 most significant events were:")
for i in range(10):
    q = data["features"][i]["properties"]
    print(f"Event: M {q['mag']:.1f} - {q['place']}, Significance: {q['sig']}")