import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Interactive Map with Folium")

# Create a Folium map centered at a specific location
map_center = [37.7749, -122.4194]  # San Francisco, CA
my_map = folium.Map(location=map_center, zoom_start=12)

# Add a marker to the map
folium.Marker([37.7749, -122.4194], popup="San Francisco").add_to(my_map)

# Display the map in Streamlit
st_folium(my_map, width=700, height=500)
