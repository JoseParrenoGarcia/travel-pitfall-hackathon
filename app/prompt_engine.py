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
  "message": "Did you mean 'London' in the United Kingdom?"
}}

### Example 2 – Correct City, Wrong Country
Input: City = "London", Country = "Germany"
Response:
{{
  "valid": false,
  "suggested_city": "London",
  "suggested_country": "United Kingdom",
  "message": "London is in the United Kingdom, not Germany."
}}

### Example 3 – City Exists in Multiple Countries
Input: City = "Springfield", Country = "USA"
Response:
{{
  "valid": true,
  "suggested_city": "Springfield",
  "suggested_country": "USA",
  "message": "Note: Springfield exists in multiple U.S. states and also in Canada and Australia. Please confirm the intended country."
}}

### Example 4 – Correct Input
Input: City = "Tokyo", Country = "Japan"
Response:
{{
  "valid": true,
  "suggested_city": "Tokyo",
  "suggested_country": "Japan",
  "message": "Tokyo in Japan is valid."
}}

### Example 5 – Non-existent City
Input: City = "Bratwurstia", Country = "Germany"
Response:
{{
  "valid": false,
  "suggested_city": null,
  "suggested_country": null,
  "message": "Bratwurstia does not appear to be a real city in Germany."
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
    # parsed_content = json.loads(content)
    # return parsed_content
    # try:
    #     parsed = eval(content)  # safe-ish since we're controlling output
    #     return parsed
    # except Exception:
    #     return {
    #         "valid": False,
    #         "suggested_city": None,
    #         "suggested_country": None,
    #         "message": "Could not parse GPT validation output.",
    #         "raw": content
    #     }

