import streamlit as st
from utils import country_list  # assumed list of 200-ish countries
from prompt_engine import validate_location

# --- PAGE CONFIG ---
st.set_page_config(page_title="What Not to Do", layout="wide")

# --- HEADER ---
st.title("What Not to Do – Travel Pitfall Briefing")
st.markdown("#### Avoid scams, cultural faux pas, and travel safety slip-ups – before they happen.")
st.markdown("---")

with st.form("input_form", border=True):
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])  # wider inputs, slimmer button

    with col1:
        city = st.text_input("City", value="London", placeholder="e.g. London")

    with col2:
        country_options = [
            f"{c['flag']} - {c['name']} ({c['code']})" for c in country_list
        ]
        default_country = "🇬🇧 - United Kingdom (GB)"
        default_index = country_options.index(default_country)
        country = st.selectbox("Country", country_options, index=default_index)

    with col3:
        tone = st.selectbox("Tone", ["Serious", "Snarky", "Funny"])

    submitted = st.form_submit_button("Validate")

# --- VALIDATION SECTION ---
confirmed = False
if submitted:
    with st.container(border=True):
        st.markdown("### Just making sure we're on the same page...")
        validation = validate_location(city, country)
        st.write(validation)
        #
        # if validation["valid"]:
        #     st.success(f"✅ {validation['message']}")
        #     confirmed = True
        # else:
        #     st.warning(f"⚠️ {validation['message']}")
        #     st.info("Please revise your input and try again.")

