# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def is_big(q):
    if q["properties"]["mag"] is not None and q["properties"]["mag"] > 5:
        return True
    return False


# Filter the data by quakes that are larger than 5 magnitude
large_quakes = list(filter(is_big, data["features"]))

# TODO: Create the header and row structures for the data
header = ["Place", "Magnitude", "Link", "Date"]
rows = []

# TODO: populate the rows with the resulting quake data
for q in large_quakes:
    the_date = datetime.date.fromtimestamp(
        int(q["properties"]["time"] / 1000))
    rows.append([q["properties"]["place"], 
                 q["properties"]["mag"],
                 q["properties"]["url"], 
                 the_date])
    


# TODO: write the results to the CSV file
with open("large_quakes.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)