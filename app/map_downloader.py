import streamlit as st
from geopy.geocoders import Nominatim

LOCATIONIQ_API_KEY = st.secrets["locationiq"]["api_key"]

@st.cache_data
def geocode_city(city: str, country: str):
    geolocator = Nominatim(user_agent="skyscanner-hackathon")
    location = geolocator.geocode(f"{city}, {country}")
    if location:
        return location.latitude, location.longitude
    return None, None

def get_osm_static_map(lat, lon, zoom=12, width=400, height=300):
    return (
        f"https://maps.locationiq.com/v3/staticmap?"
        f"key={LOCATIONIQ_API_KEY}&center={lat},{lon}"
        f"&zoom={zoom}&size={width}x{height}&format=png&markers=icon:small-red-cutout|{lat},{lon}"
    )