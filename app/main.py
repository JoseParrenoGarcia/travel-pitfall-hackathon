import streamlit as st
from utils import country_list  # assumed list of 200-ish countries
from prompt_engine import validate_location, generate_city_snippet
from image_downloader import get_city_image_url
from map_downloader import geocode_city, get_osm_static_map

# --- PAGE CONFIG ---
st.set_page_config(page_title="What Not to Do", layout="wide")

# --- SESSION STATE DEFAULTS ---
if "validation" not in st.session_state:
    st.session_state.validation = None
if "city" not in st.session_state:
    st.session_state.city = ""
if "country" not in st.session_state:
    st.session_state.country = ""
if "confirmed" not in st.session_state:
    st.session_state.confirmed = False

# --- HEADER ---
st.title("What Not to Do – Travel Pitfall Briefing")
st.markdown("#### Avoid scams, cultural faux pas, and travel safety slip-ups – before they happen.")

with st.form("input_form", border=True):
    col1, col2, col3 = st.columns([1, 1, 4])  # wider inputs, slimmer button

    with col1:
        city = st.text_input("City", value=st.session_state.city or "London", placeholder="e.g. London")

    with col2:
        country_options = [
            f"{c['flag']} - {c['name']} ({c['code']})" for c in country_list
        ]
        default_country = "🇬🇧 - United Kingdom (GB)"
        default_index = country_options.index(default_country)
        country = st.selectbox("Country", country_options, index=default_index)

    submitted = st.form_submit_button("Validate")
    if submitted:
        st.session_state.city = city
        st.session_state.country = country
        st.session_state.validation = validate_location(city, country)
        st.session_state.confirmed = False  # Reset confirmation after new validation

# --- VALIDATION SECTION ---
if st.session_state.validation:
    with st.container(border=True):
        st.markdown("##### Just making sure we are on the same page...")
        validation = validate_location(city, country)

        if st.session_state.validation["valid"]:
            st.success(st.session_state.validation["message"])

            if st.button("Proceed to tips", key="confirmed_button"):
                st.session_state.confirmed = True
        else:
            st.warning(st.session_state.validation['message'])
            st.info("Please revise your input and try again.")

# --- SNAPSHOT SECTION ---
if st.session_state.confirmed:
    with st.container(border=True):
        st.markdown("##### Destination Snapshot")

        snippet = generate_city_snippet(city, country)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"**City:** {city}")
            st.markdown(f"**Country:** {country}")
            st.markdown(f"_{snippet}_")

        with col2:
            image_url, attribution = get_city_image_url(city)
            if image_url:
                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        <img src="{image_url}" alt="Photo by {attribution['photographer']} on Unsplash" style="height:420px; width:auto;">
                        <p>Photo by {attribution['photographer']} on Unsplash</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                # st.image(image_url, caption=f"Photo by {attribution['photographer']} on Unsplash", use_container_width=True)
                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        Source: <a href="{attribution['profile_url']}" target="_blank">Unsplash</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.write("No image available.")


        with col3:
            lat, lon = geocode_city(city=city, country=st.session_state.validation["suggested_country"])
            st.image(get_osm_static_map(lat, lon), caption="Map location", use_container_width=True)


