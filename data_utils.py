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

<<<<<<< HEAD
Geocoder(collapsed = False, add_marker = True).add_to(my_map)

circle_script = """
function onSearchFound(e) {
    var lat = e.result.center[0];  // Latitude of the found location
    var lon = e.result.center[1];  // Longitude of the found location

    // Create a circle with a 5-mile radius (about 8046.7 meters)
    L.circle([lat, lon], {
        color: 'red',
        fillColor: '#007BFF',
        fillOpacity: 0.2,
        radius: 8046.7  // 5 miles in meters
    }).addTo(map);
}
"""


def get_home_button():
    from flask import url_for
    from app import app
    
    with app.app_context():
        home_url = url_for('home')
        
    home_button_html = """
        <form action="{home_url}" method="POST">
        <button type="submit">⬅ Back to Home</button>
        </form>
    """
    return home_button_html


# Add the JavaScript to handle circle creation on search result
my_map.get_root().html.add_child(Element(f"""
<script>
    {circle_script}
</script>
"""))


def get_home_button():
    from flask import url_for
    from app import app
    
    with app.app_context():
        home_url = url_for('home')
        
    home_button_html = """
        <form action="{home_url}" method="POST">
        <button type="submit">⬅ Back to Home</button>
        </form>
    """
    return home_button_html

# Add the button to the bottom of the HTML (after the map)
home_btn = get_home_button()
my_map.get_root().html.add_child(Element(home_btn))

=======
>>>>>>> parent of 1972bb4 (added search bar and the home button)
my_map.save("templates/crime_map.html")