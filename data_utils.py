import json, folium, random
from folium.plugins import MarkerCluster, Geocoder
from folium import Element




with open("cleaned_crimes.json") as f:
    data = json.load(f)
    
locations = []

for item in data:
    locations.append((item['LATITUDE'], item['LONGITUDE']))
    
    
my_map = folium.Map(location=[41.8781, - 87.6298], zoom_start= 15)

size = int(0.1 * len(locations))
random_sample = random.sample(locations, size)


marker_cluster = MarkerCluster().add_to(my_map)

for item in random_sample:
    folium.Marker(item, popup='Marker Label').add_to(marker_cluster)

Geocoder(collapsed = False, add_marker = True).addTo(my_map)

home_button_html = """
<div style="text-align: center; margin-top: 20px;">
    <button onclick="window.location.href='home.html'"
        style="
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        ">
        ⬅ Back to Home
    </button>
</div>
"""

# Add the button to the bottom of the HTML (after the map)
my_map.get_root().html.add_child(Element(home_button_html))

my_map.save("templates/crime_map.html")