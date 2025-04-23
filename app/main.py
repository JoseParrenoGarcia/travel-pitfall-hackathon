import streamlit as st
from utils import country_list  # assumed list of 200-ish countries
from prompt_engine import validate_location

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
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])  # wider inputs, slimmer button

    with col1:
        city = st.text_input("City", value=st.session_state.city or "London", placeholder="e.g. London")

    with col2:
        country_options = [
            f"{c['flag']} - {c['name']} ({c['code']})" for c in country_list
        ]
        default_country = "🇬🇧 - United Kingdom (GB)"
        default_index = country_options.index(default_country)
        country = st.selectbox("Country", country_options, index=default_index)

    # with col3:
    #     tone = st.selectbox("Tone", ["Serious", "Snarky", "Funny"])

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
        st.write(validation)

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

        # snippet = generate_city_snippet(city, country, tone)

        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     st.markdown(f"**City:** {city}")
        #     st.markdown(f"**Country:** {country}")
        #     st.markdown(f"_{snippet}_")
        #
        # with col2:
        #     st.image("assets/city_placeholder.png", caption="City view")
        #
        # with col3:
        #     st.image("assets/map_placeholder.png", caption="Map location")


