import json

with open("cleaned_crimes.json") as f:
    data = json.load(f)
    
locations = []

for item in data:
    locations.append((item['LATITUDE'], item['LONGITUDE']))