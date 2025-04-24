# 🌍 What Not to Do – Travel Pitfall Briefing

An AI-powered travel assistant that helps you avoid scams, etiquette slip-ups, and safety issues when exploring new destinations — built with love at the Skyscanner Hackathon 💙

---

## ✨ Features

- 🧠 Smart destination validation (typo correction, country mismatch detection)
- 🔎 GPT-4 powered tips across 6 themes: Transport, Food, Money, Culture, Safety, and Health
- 📸 City photo pulled dynamically from Unsplash
- 🗺️ Static map snapshot via OpenStreetMap (LocationIQ)
- 💡 Tips written in a helpful, local-savvy tone
- 🎨 Clean Streamlit UI with a validation step, snapshot section, and structured output

---

## 🧱 Tech Stack

- 🐍 Python 3.9+
- ⚡ Streamlit
- 🧠 OpenAI GPT-4 API (`gpt-4-0125-preview`)
- 📷 Unsplash API
- 🗺️ LocationIQ Static Maps + Nominatim Geocoding
- 🗃️ Cached API calls with `st.cache_data`
- 💙 Styled UI with custom footer

---

## 📸 Preview

![App Demo](assets/APP-video.gif)

---

## 🚀 Running the App

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/travel-pitfall-hackathon.git
cd travel-pitfall-hackathon
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up secrets:**
Create a file at .streamlit/secrets.toml with your keys
```toml
[openai]
api_key = "sk-..."

[unsplash]
api_key = "..."

[locationiq]
api_key = "..."
```

4. **Run the app:**
```bash
streamlit run app/main.py
```


## 🧠 How It Works
The app runs in 4 stages:

- Validation – Checks if the city + country combo is valid, fixes spelling, and prevents hallucination.
- Snapshot – Shows a short GPT-generated summary of the city, a photo from Unsplash, and a map via LocationIQ.
- Tips – GPT-4 generates structured travel advice across 6 themed categories.
- Final Section – Tips are displayed in two rows of 3 columns, grouped and styled for readability.

## 💡 Future Ideas

- PDF / Shareable Card Export
- Tone selector (snarky, funny, corporate)
- Local LLM fallback (Gemma / Ollama support)
- Multilingual support
- Scams verification via scraping news or forums

## 🧑‍💻 Hackathon Team
Built with ❤️ by your friendly neighbourhood Skyscanner Hackathon crew
Powered by OpenAI, Streamlit, Unsplash, and OpenStreetMap