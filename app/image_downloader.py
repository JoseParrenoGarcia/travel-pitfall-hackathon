import streamlit as st
import requests

UNSPLASH_API_KEY = st.secrets["unsplash"]["api_key"]

@st.cache_data(show_spinner=False)
def get_city_image_url(city: str) -> str:
    endpoint = "https://api.unsplash.com/search/photos"
    params = {
        "query": f"{city} city",
        "client_id": UNSPLASH_API_KEY,
        "per_page": 1,
        "orientation": "landscape"
    }

    response = requests.get(endpoint, params=params)
    response.raise_for_status()  # Raise an error for bad status codes (e.g., 403, 404)

    data = response.json()
    if data.get("results"):
        photo = data["results"][0]
        image_url = photo["urls"]["regular"]  # Use 'regular' for balanced quality
        attribution = {
            "photographer": photo["user"]["name"],
            "profile_url": f"{photo['user']['links']['html']}?utm_source=your_app_name&utm_medium=referral"
        }
        return image_url, attribution

    else:
        st.warning(f"No images found for {city}.")
        return None, None

