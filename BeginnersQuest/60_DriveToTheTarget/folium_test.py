import folium

theme =  ["OpenStreetMap", "Stamen Terrain", "Stamen Toner", "Mapbox Bright", "Mapbox Control Room"]
selected_theme_index = 0
selected_theme = theme[selected_theme_index]
location = [51.523910, -0.158578]

m = folium.Map(location=location,
               tiles=selected_theme,
               zoom_start=10)
               
folium.Circle(
    location=location,
    radius=50,
    popup='Holmes Home',
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
).add_to(m)
m.add_child(folium.ClickForMarker())
m.save("map.html")

"""
<html>
<body style="background:#888888">
</body>
</html>
"""