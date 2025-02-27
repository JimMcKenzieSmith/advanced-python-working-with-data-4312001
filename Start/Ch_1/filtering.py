# Example file for Advanced Python: Working With Data by Joe Marini
# using the filter() function to filter a data set

import json


def filterEvens(x):
    # filters out even numbers and keeps odd numbers
    if x % 2 == 0:
        return False
    return True


def filterUppers(x):
    # filters out upper-case letters and keeps lower case letters
    if x.isupper():
        return False
    return True


# define some sample sequences to operate on
nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
chars = "abcDeFGHiJklmnoP"

# TODO: use filter to remove items from a list
odds = list(filter(filterEvens, nums))
print(f"Odds {odds}")

# TODO: use filter on non-numeric sequence
lowers = list(filter(filterUppers, chars))
print("lowers",lowers)

# Use the filter on our data - let's filter out all seismic events that were *not* quakes
# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def not_a_quake(q):
    if q["properties"]["type"] == "earthquake":
        return False
    return True
    
result = list(filter(not_a_quake, data["features"]))
print(f"Total non-quake events: {len(result)}")
for idx, q in enumerate(result):
    print(idx+1, q["properties"]["type"])
    if idx == 9: break