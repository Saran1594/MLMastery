# REading a CSV file
import csv
from pprint import pprint
with open("C:\\Users\\JW60\\OneDrive - Nordstrom\\Panda.csv","r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    zones = list(reader)
    for zone in zones:
        zone["PPH"] = int(zone["PPH"])
        zone["Target_PPH"] = int(zone["Target_PPH"])
sorter_zone = sorted(zones,key= lambda zone:zone["PPH"])
top_zones = sorter_zone[-3:]
top_zones_reversed = top_zones[::-1]
pprint(top_zones_reversed)
