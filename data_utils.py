import json
import folium;

with open("cleaned_crimes.json") as f:
    data = json.load(f)
    
locations = []

for item in data:
    locations.append((item['LATITUDE'], item['LONGITUDE']))


my_map = folium.Map(location=[41.8781, - 87.6298], zoom_start= 10)

for item in locations:
    folium.Marker(item, popup='Marker Label').add_to(my_map)

my_map.save("crime_map.html")