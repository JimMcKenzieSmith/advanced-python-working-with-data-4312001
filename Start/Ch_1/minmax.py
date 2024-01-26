# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
print(f"The minimum value is: {min(values)}")
print(f"The minimum value is: {min(strings)}")

# TODO: The max() function finds the maximum value
print(f"The maximum value is: {max(values)}")
print(f"The maximum value is: {max(strings)}")

# TODO: define a custom "key" function to extract a data field
print(f"The minimum value is: {min(strings, key=len)}")
print(f"The maximum value is: {max(strings, key=len)}")

# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
# find the largest and smallest earthquakes, as measured by magnitude
print(data["features"][0]["properties"]["mag"])
min_mag = 2 ** 32
max_mag = 0


def get_mag(data_item):
    mag = data_item["properties"]["mag"]
    if mag is None:
        mag = 0
    return float(mag)

for feature in data["features"]:
    # mag_raw = feature["properties"]["mag"]
    # mag = mag_raw if mag_raw != None else 0
    mag = get_mag(feature)
    min_mag = min(min_mag, mag)
    max_mag = max(max_mag, mag)
print(f"The min magnitude is {min_mag} and the max magnitude is {max_mag}")
print(f"The minimum value using a key function is {min(data['features'], key=get_mag)}")
print(f"The max value using a key function is {max(data['features'], key=get_mag)}")