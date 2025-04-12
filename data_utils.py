import json, folium, random
from folium.plugins import MarkerCluster

with open("cleaned_crimes.json") as f:
    data = json.load(f)
    
locations = []

for item in data:
    locations.append((item['LATITUDE'], item['LONGITUDE']))


my_map = folium.Map(location=[41.8781, - 87.6298], zoom_start= 10)

size = int(0.1 * len(locations))
random_sample = random.sample(locations, size)


marker_cluster = MarkerCluster().add_to(my_map)

for item in random_sample:
    folium.Marker(item, popup='Marker Label').add_to(marker_cluster)

my_map.save("crime_map.html")