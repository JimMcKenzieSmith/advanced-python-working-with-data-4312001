# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map link"]
def get_sig(q):
    return q["properties"]["sig"]

# sort quakes by significance
quakes = sorted(data["features"], key=get_sig, reverse=True)

top_40_quakes = quakes[:40]

def get_time(q):
    return int(q["properties"]["time"])

top_40_quakes.sort(key=get_time, reverse=True)
rows = []
for q in top_40_quakes:
    felt = q["properties"]["felt"] if q["properties"]["felt"] != None else 0
    rows.append([q["properties"]["mag"],
                 q["properties"]["place"],
                 felt,
                 datetime.date.fromtimestamp(int(q["properties"]["time"] / 1000)),
                 "https://www.google.com/maps/search/?api=1&query=" + 
                 str(q["geometry"]["coordinates"][1]) + "%2C" + 
                 str(q["geometry"]["coordinates"][0])
                 ])

with open("top_40.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)
