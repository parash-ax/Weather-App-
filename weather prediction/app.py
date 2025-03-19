import streamlit as st
import requests

# OpenWeatherMap API Key
API_KEY = "bd5e378503939ddaee76f12ad7a97608"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather details for a given city"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Weather": data["weather"][0]["description"].title(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
    else:
        return None

# 🎨 Streamlit Theme Customization
st.set_page_config(page_title="Weather App ☀️", page_icon="🌦", layout="centered")

# 🌈 App Title with Styling
st.markdown(
    """
    <h1 style='text-align: center; color: #305590;'>🌦 Weather App</h1>
    <p style='text-align: center; color: #ffffff;'>Get real-time weather updates for any city! 🌍</p>
    """,
    unsafe_allow_html=True,
)

# 🏙 User Input for City Name
city_name = st.text_input("🔍 Enter City Name", placeholder="E.g., New York, Tokyo, Mumbai", help="Type a city name and press enter")

# 🎨 Background Styling
st.markdown(
    """
    <style>
        body {
            background-color: #F0F8FF;
        }
        .stApp {
            background: linear-gradient(to right, #6a667c, #19c0e6);
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🌤 Get Weather Button
if st.button("☁️ Get Weather"):
    if city_name:
        weather_info = get_weather(city_name)
        if weather_info:
            # 🎨 Styled Container
            st.markdown(
                f"""
                <div style="border-radius: 15px; padding: 20px; background-color: #305590; color: white; text-align: center;">
                    <h2>📍 {weather_info['City']}</h2>
                    <h3>🌡 Temperature: {weather_info['Temperature']}</h3>
                    <h3>⛅ Weather: {weather_info['Weather']}</h3>
                    <h3>💧 Humidity: {weather_info['Humidity']}</h3>
                    <h3>🌬 Wind Speed: {weather_info['Wind Speed']}</h3>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.error("❌ City not found. Please check the name.")
    else:
        st.warning("⚠️ Please enter a city name.")

# 🎨 Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: #414246;'>PARASHRAM ❤️ Weather app</p>
    """,
    unsafe_allow_html=True,
)

