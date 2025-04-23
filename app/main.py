import streamlit as st
from utils import country_list  # assumed list of 200-ish countries

# --- PAGE CONFIG ---
st.set_page_config(page_title="What Not to Do", layout="wide")

# --- HEADER ---
st.title("What Not to Do – Travel Pitfall Briefing")
st.markdown("#### Avoid scams, cultural faux pas, and travel safety slip-ups – before they happen.")
st.markdown("---")

with st.form("input_form", border=True):
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])  # wider inputs, slimmer button

    with col1:
        city = st.text_input("City", placeholder="e.g. London")

    with col2:
        country_options = [
            f"{c['flag']} - {c['name']} ({c['code']})" for c in country_list
        ]
        country = st.selectbox("Country", country_options)

    with col3:
        tone = st.selectbox("Tone", ["Serious", "Snarky", "Funny"])

    submitted = st.form_submit_button("Validate")
