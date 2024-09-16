import folium
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)
html_path = os.path.join(assets_dir, 'mapa.html')

m = folium.Map(location=[-23.55052, -46.633308], zoom_start=12)

folium.Marker(
    location=[-23.55052, -46.633308],
    popup='São Paulo, Brasil',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Circle(
    location=[-23.55052, -46.633308],
    radius=500,
    popup='Centro de São Paulo',
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(m)

folium.CircleMarker(
    location=[-23.55052, -46.633308],
    radius=50,
    popup='Centro de São Paulo',
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
).add_to(m)

m.save(html_path)