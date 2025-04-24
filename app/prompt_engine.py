from openai import OpenAI
from utils import safe_json_parse
import streamlit as st


OPENAI_API_KEY = st.secrets["openai"]["api_key"]
OPENAI_MODEL = st.secrets["openai"]["model"]

client = OpenAI(api_key=OPENAI_API_KEY)

# --- PROMPT TEMPLATE FOR LOCATION VALIDATION ---
def build_location_validation_prompt(city: str, country: str) -> str:
    return f"""
You are a location validation assistant. A user has entered a city and a country. Your job is to:
1. Check if the city exists.
2. Check if the city matches the country.
3. If not, suggest correct spellings or country matches.
4. If the city is ambiguous (exists in multiple countries), list alternatives.
5. Respond in strict JSON format.

Here are some examples:

### Example 1 – Misspelled City
Input: City = "Lnodon", Country = "United Kingdom"
Response:
{{
  "valid": false,
  "suggested_city": "London",
  "suggested_country": "United Kingdom",
  "message": "⚠️ Did you mean **London** in the United Kingdom?"
}}

### Example 2 – Correct City, Wrong Country
Input: City = "London", Country = "Germany"
Response:
{{
  "valid": false,
  "suggested_city": "London",
  "suggested_country": "United Kingdom",
  "message": "⚠️ I think you are referring to **London** which is in the **United Kingdom**, not in ***Germany.***"
}}

### Example 3 – Correct Input
Input: City = "Tokyo", Country = "Japan"
Response:
{{
  "valid": true,
  "suggested_city": "Tokyo",
  "suggested_country": "Japan",
  "message": "✅ Looks like we are on the same page! I recognise **Tokyo** as a city in **Japan**."
}}

### Example 4 – Non-existent City
Input: City = "Bratwurstia", Country = "Germany"
Response:
{{
  "valid": false,
  "suggested_city": null,
  "suggested_country": null,
  "message": "⚠️ Bratwurstia does not appear to be a real city in Germany."
}}

Now validate this location:
Input: City = "{city}", Country = "{country}"
Respond only in JSON. Do not explain anything else.
"""


@st.cache_data(show_spinner=False)
def validate_location(city: str, country: str) -> dict:
    prompt = build_location_validation_prompt(city, country)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful travel assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    content = response.choices[0].message.content
    return safe_json_parse(content)


# --- PROMPT TEMPLATE FOR CITY SNIPPET ---
def build_city_snippet_prompt(city: str, country: str) -> str:
    return f"""
You are a travel guide assistant.

Describe the city "{city}" in "{country}" in one paragraph.
Make it engaging and friendly, like a travel brochure.
Avoid safety tips, scams, or etiquette. Focus only on the vibe, landmarks, or general character of the place.
Keep the description under 200 words.
"""

@st.cache_data(show_spinner=False)
def generate_city_snippet(city: str, country: str) -> str:
    prompt = build_city_snippet_prompt(city, country)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful travel guide assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
    )

    return response.choices[0].message.content.strip()

def build_travel_tips_prompt(city: str, country: str) -> str:
    return f"""
You are a travel safety and culture assistant. The user is visiting {city} in {country}.

Provide a structured JSON response with exactly these six fields:
- "transport": Tips on navigating the city, safe/unsafe areas, taxis, apps, strikes, cycling, driving customs.
- "food": Local food culture, tipping habits, tap water safety, what to eat or avoid, dining etiquette.
- "money": Payment methods, local currency traps, scams, where to exchange, when to use cash vs card.
- "culture": Language customs, local gestures, noise levels, queuing habits, clothing norms, taboos, alcohol, pork or cow meat.
- "safety": General safety tips, avoiding theft, safe areas, travel insurance, solo travel awareness.
- "health": Hydration, sun protection, heat risks, first aid, pharmacies, vaccinations, bottled vs tap water.

Each field should contain 5 concise bullet points. If not enough relevant advice exists for that theme in this location, include fewer — but never fabricate tips.

Be **local**, **practical**, and **direct** — not generic. Include:
- Specific local behaviors (“stand on the right side of the escalator”)
- Typical red flags (“menu with pictures in tourist zones = avoid”)
- Local insider tips (“paella doesn’t have chorizo”)
- Avoid generic advice
- Do not invent scams. Only include well-known scams or typical tourist traps that are reasonably likely in {city}. If unsure, omit it.
- Avoid repeating advice across sections. If you mention a taxi app under “Safety”, don’t mention it again under “Scams”.

Here are some common themes and examples to inspire your bullet points:

- Transport: taxi apps, metro etiquette, transport strikes, left/right driving, bike safety, ride scams.
- Brands: When recommending tools or services (e.g. taxi apps), use specific brand names that are known and local — e.g. Cabify in Spain, Grab in SE Asia, Bolt in Eastern Europe, Uber in the UK/US.
- Food & Drink: tipping, restaurant red flags, authentic vs. tourist menus, local dishes, tap water is accepted (or the default is bottled water), Tripadvisor is your best friend.
- Money: cash vs card, ATM scams, dynamic currency conversion, overcharging.
- Culture: dress code, noise levels, queueing, political sensitivity, language etiquette.
- Safety: pickpockets, dangerous areas, solo traveler tips, late-night travel.  
- Health:  sun cream and cap, avoid midday high temperatures, ensure you have medical coverage, tap water safety.
- Tourist traps: photo scams, fake tickets, street performers, bracelet scammers.

Write in a **natural, friendly tone**, like you’re giving real advice to a smart friend. Do not include intros or explanations — just return pure JSON.
"""


@st.cache_data(show_spinner=False)
def fetch_tips(city: str, country: str) -> dict:
    prompt = build_travel_tips_prompt(city, country)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful travel safety assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    content = response.choices[0].message.content
    return safe_json_parse(content)