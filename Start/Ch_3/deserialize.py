# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open("large_quakes.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    sniffer = csv.Sniffer()
    sample = csv_file.read(1024)
    csv_file.seek(0)
    if sniffer.has_header(sample):
        next(reader) #skips the first row (header row)
    for r in reader:
        # print(r)
        result.append({
            "place": r[0],
            "mag": r[1],
            "date": r[2],
            "link": r[3]
        })

pprint.pp(result)
